import React, { useState, useCallback } from 'react';
import { Upload, X, Loader2, Image as ImageIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

interface ImageUploadProps {
  onImageSelect: (file: File, previewUrl: string) => void;
  isAnalyzing: boolean;
}

const ImageUpload: React.FC<ImageUploadProps> = ({ onImageSelect, isAnalyzing }) => {
  const [preview, setPreview] = useState<string | null>(null);
  const [isDragging, setIsDragging] = useState(false);

  const handleFile = useCallback((file: File) => {
    if (!file.type.startsWith('image/')) {
      return;
    }

    const reader = new FileReader();
    reader.onload = () => {
      const result = reader.result as string;
      setPreview(result);
      onImageSelect(file, result);
    };
    reader.readAsDataURL(file);
  }, [onImageSelect]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const file = e.dataTransfer.files[0];
    if (file) {
      handleFile(file);
    }
  }, [handleFile]);

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const handleFileInput = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      handleFile(file);
    }
  }, [handleFile]);

  const clearPreview = () => {
    setPreview(null);
  };

  return (
    <div className="w-full">
      {!preview ? (
        <div
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          className={cn(
            "relative border-2 border-dashed rounded-2xl p-12 text-center transition-all duration-300 cursor-pointer",
            isDragging 
              ? "border-primary bg-primary/5 scale-[1.02]" 
              : "border-border hover:border-primary/50 hover:bg-secondary/50"
          )}
        >
          <input
            type="file"
            accept="image/*"
            onChange={handleFileInput}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          />
          <div className="space-y-4">
            <div className="mx-auto w-16 h-16 rounded-2xl gradient-primary flex items-center justify-center shadow-glow">
              <Upload className="w-8 h-8 text-primary-foreground" />
            </div>
            <div>
              <p className="text-lg font-semibold text-foreground mb-1">
                Upload Skin Image
              </p>
              <p className="text-sm text-muted-foreground">
                Drag and drop or click to browse
              </p>
            </div>
            <p className="text-xs text-muted-foreground">
              Supports: JPG, PNG, WEBP • Max size: 10MB
            </p>
          </div>
        </div>
      ) : (
        <div className="relative rounded-2xl overflow-hidden bg-secondary/30 border border-border">
          <img 
            src={preview} 
            alt="Preview" 
            className="w-full h-64 object-contain bg-card"
          />
          {!isAnalyzing && (
            <button
              onClick={clearPreview}
              className="absolute top-3 right-3 p-2 bg-card/90 backdrop-blur-sm rounded-full shadow-lg hover:bg-destructive hover:text-destructive-foreground transition-colors"
            >
              <X className="w-4 h-4" />
            </button>
          )}
          {isAnalyzing && (
            <div className="absolute inset-0 bg-card/80 backdrop-blur-sm flex items-center justify-center">
              <div className="text-center space-y-3">
                <Loader2 className="w-10 h-10 text-primary animate-spin mx-auto" />
                <p className="text-sm font-medium text-foreground">Analyzing image...</p>
                <p className="text-xs text-muted-foreground">AI is detecting skin conditions</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ImageUpload;
