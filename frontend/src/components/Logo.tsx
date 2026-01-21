import React from 'react';
import { Activity, Shield, Heart } from 'lucide-react';

const Logo: React.FC<{ className?: string }> = ({ className }) => {
  return (
    <div className={`flex items-center gap-2 ${className}`}>
      <div className="relative">
        <div className="w-10 h-10 rounded-xl gradient-primary flex items-center justify-center shadow-glow">
          <Activity className="w-5 h-5 text-primary-foreground" />
        </div>
        <div className="absolute -bottom-0.5 -right-0.5 w-4 h-4 bg-accent rounded-full flex items-center justify-center">
          <Heart className="w-2.5 h-2.5 text-accent-foreground" />
        </div>
      </div>
      <div className="flex flex-col">
        <span className="text-lg font-bold text-foreground leading-tight">DermaCare</span>
        <span className="text-xs text-muted-foreground leading-tight">AI Diagnostics</span>
      </div>
    </div>
  );
};

export default Logo;
