import React from 'react';
import { Calendar, Clock, ChevronRight, Trash2 } from 'lucide-react';
import { cn } from '@/lib/utils';
import { format } from 'date-fns';
import { supabase } from '@/lib/supabase';

interface HistoryListProps {
  items: any[];
  onSelectItem: (item: any) => void;
  onDeleteSuccess?: () => void; // Optional callback to refresh the list
}

const HistoryList: React.FC<HistoryListProps> = ({ items, onSelectItem, onDeleteSuccess }) => {
  
  // Helper to handle record deletion from Supabase
  const handleDelete = async (e: React.MouseEvent, id: string) => {
    e.stopPropagation(); // Prevent triggering onSelectItem
    
    if (window.confirm("Are you sure you want to delete this scan?")) {
      const { error } = await supabase
        .from('scans')
        .delete()
        .eq('id', id);

      if (!error && onDeleteSuccess) {
        onDeleteSuccess();
      }
    }
  };

  if (items.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="w-16 h-16 rounded-full bg-slate-50 mx-auto flex items-center justify-center mb-4">
          <Clock className="w-8 h-8 text-slate-300" />
        </div>
        <h3 className="text-lg font-bold text-slate-900 mb-2">No History Yet</h3>
        <p className="text-slate-500 max-w-sm mx-auto text-sm">
          Your cloud-synced history will appear here once you've completed an analysis.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {items.map((item) => (
        <div
          key={item.id}
          className="group relative bg-white rounded-2xl border border-slate-100 p-4 hover:shadow-md transition-all duration-300 cursor-pointer"
          onClick={() => onSelectItem(item)}
        >
          <div className="flex gap-4">
            {/* Supabase image_url usage */}
            <img 
              src={item.image_url} 
              alt="Scan"
              className="w-20 h-20 rounded-xl object-cover bg-slate-100"
            />
            
            <div className="flex-1 min-w-0">
              <div className="flex items-start justify-between">
                <div>
                  <h4 className="font-bold text-slate-900 text-lg truncate pr-8">
                    {item.disease}
                  </h4>
                  <div className="flex items-center gap-2 mt-1">
                    <span className="text-xs font-bold text-primary bg-primary/10 px-2 py-0.5 rounded-full">
                      {item.confidence.toFixed(1)}% Confidence
                    </span>
                  </div>
                </div>
                
                <div className="flex items-center gap-2">
                   {/* Delete Button */}
                  <button 
                    onClick={(e) => handleDelete(e, item.id)}
                    className="p-2 text-slate-300 hover:text-red-500 hover:bg-red-50 rounded-lg transition-colors"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                  <ChevronRight className="w-5 h-5 text-slate-300 group-hover:text-primary transition-colors" />
                </div>
              </div>

              <div className="flex items-center gap-4 mt-3 text-xs text-slate-400">
                <span className="flex items-center gap-1">
                  <Calendar className="w-3.5 h-3.5" />
                  {/* format date from Supabase created_at */}
                  {item.created_at ? format(new Date(item.created_at), 'MMM d, yyyy') : 'Recently'}
                </span>
                {item.location && (
                  <span className="truncate">
                    {item.location.city}, {item.location.state}
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default HistoryList;