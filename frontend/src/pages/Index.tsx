import React from 'react';
import { Link } from 'react-router-dom';
import { Camera, Zap, Heart, ShieldCheck, Lock, Activity, ClipboardCheck } from 'lucide-react';
import { Button } from '@/components/ui/button';
import Logo from '@/components/Logo';

const Index: React.FC = () => {
  return (
    <div className="min-h-screen bg-[#FDFDFF] text-slate-900 selection:bg-primary/10 overflow-x-hidden">
      {/* Navigation */}
      <header className="container mx-auto px-8 py-6 flex items-center justify-between relative z-50">
        <Logo />
        <div className="flex items-center gap-6">
          <Link to="/login" className="text-sm font-semibold text-slate-500 hover:text-primary transition-colors">
            Sign In
          </Link>
          <Link to="/register">
            <Button variant="gradient" size="sm" className="rounded-full px-8 shadow-sm font-bold transition-transform hover:scale-105">
              Get Started
            </Button>
          </Link>
        </div>
      </header>

      <main className="container mx-auto px-8">
        <div className="flex flex-col lg:flex-row items-center justify-between gap-16 py-12 lg:py-24">
          
          {/* Left Content */}
          <div className="lg:w-5/12 space-y-8">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-[11px] font-bold uppercase tracking-wider">
              <span className="flex h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
              Clinical-Grade Dermatology AI
            </div>
            
            <h1 className="text-4xl md:text-5xl font-bold tracking-tight leading-[1.2] text-slate-900">
              Your skin’s health, <br />
              <span className="text-primary italic font-serif">reimagined.</span>
            </h1>
            
            <p className="text-base md:text-lg text-slate-500 leading-relaxed max-w-sm">
              AI-powered skin analysis with instant insights and professional doctor recommendations.
            </p>
            
            <div className="pt-2">
              <Link to="/register">
                <Button variant="gradient" size="lg" className="rounded-full shadow-xl shadow-primary/20 hover:shadow-primary/30 transition-all px-10 py-7 text-lg group">
                  Start Analysis <Camera className="ml-3 w-5 h-5 group-hover:rotate-12 transition-transform" />
                </Button>
              </Link>
            </div>
          </div>

          {/* Right Content: Professional Skin Scanning Visual */}
          <div className="lg:w-6/12 relative flex justify-center lg:justify-end">
            
            {/* The Scanning Container */}
            <div className="relative z-10 w-full aspect-square max-w-[440px] overflow-hidden rounded-[3.5rem] shadow-2xl border-[8px] border-white bg-white">
              
              {/* Professional Skin Examination Image */}
              <img 
                src="https://media.istockphoto.com/id/169952306/photo/skin-allergy.webp?a=1&b=1&s=612x612&w=0&k=20&c=k7Jy1SAdqFtKBIxCpuLCEeqtnL0sBtQyLQ_0ox3ed0o=" 
                alt="Clinical skin examination" 
                className="w-full h-full object-cover grayscale-[10%] contrast-[1.05]"
              />

              {/* The Scanning UI Overlay */}
              <div className="absolute inset-0 flex items-center justify-center p-16">
                <div className="relative w-full h-full border border-white/40 rounded-2xl backdrop-blur-[0.5px]">
                  
                  {/* Viewfinder Corners */}
                  <div className="absolute -top-1 -left-1 w-10 h-10 border-t-[4px] border-l-[4px] border-primary rounded-tl-lg" />
                  <div className="absolute -top-1 -right-1 w-10 h-10 border-t-[4px] border-r-[4px] border-primary rounded-tr-lg" />
                  <div className="absolute -bottom-1 -left-1 w-10 h-10 border-b-[4px] border-l-[4px] border-primary rounded-bl-lg" />
                  <div className="absolute -bottom-1 -right-1 w-10 h-10 border-b-[4px] border-r-[4px] border-primary rounded-br-lg" />
                  
                  {/* Animated Laser Scan Line */}
                  <div className="absolute top-0 left-0 w-full h-[2px] bg-primary shadow-[0_0_20px_rgba(var(--primary-rgb),1)] animate-scan-move" />
                </div>
              </div>
            </div>

            {/* --- THREE FLOATING CARDS --- */}

            {/* 1. Status Card (Top Left) */}
            <div className="absolute -left-10 top-12 z-20 bg-white/95 backdrop-blur-md p-5 rounded-3xl shadow-xl border border-white/50 w-60 animate-float">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-2xl bg-primary flex items-center justify-center shadow-lg shadow-primary/20">
                  <Activity className="text-white w-6 h-6" />
                </div>
                <div>
                  <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Diagnostic AI</p>
                  <p className="text-sm font-bold text-slate-800">High Precision</p>
                </div>
              </div>
            </div>

            {/* 2. NEW: Medical Verification Card (Bottom Right) */}
            <div className="absolute -right-6 bottom-6 z-20 bg-white p-4 rounded-3xl shadow-2xl border border-slate-50 w-44 animate-float-delayed">
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-primary/10 flex items-center justify-center">
                  <ClipboardCheck className="text-primary w-5 h-5" />
                </div>
                <div>
                  <p className="text-[10px] font-black text-slate-800 uppercase leading-none">Recommendations</p>
                  <p className="text-[9px] text-slate-400 font-bold uppercase tracking-tighter">Nearby clinics</p>
                </div>
              </div>
            </div>

            {/* 3. Privacy/HIPAA Card (Lower Left) */}
            <div className="absolute -left-6 bottom-10 z-20 bg-white p-4 rounded-2xl shadow-lg border border-slate-50 w-52 animate-float-slow">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-lg bg-slate-100 flex items-center justify-center">
                  <ShieldCheck className="text-slate-500 w-5 h-5" />
                </div>
                <div>
                  <p className="text-[10px] font-bold text-slate-800 uppercase text-center">Data Secure</p>
                  <p className="text-[10px] text-slate-400 font-medium">100% Confidential</p>
                </div>
              </div>
            </div>

            {/* Ambient Background Glow */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-primary/10 blur-[120px] -z-10 rounded-full" />
          </div>
          
        </div>
      </main>

      {/* Small Minimal Footer */}
      <footer className="py-10 mt-12 border-t border-slate-100">
        <div className="container mx-auto px-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-[10px] font-bold text-slate-300 uppercase tracking-[0.4em]">
            © 2026 DermaCare Systems
          </p>
          <div className="flex gap-8 text-[10px] font-bold text-slate-400 uppercase tracking-widest">
            <a href="#" className="hover:text-primary transition-colors">Privacy</a>
            <a href="#" className="hover:text-primary transition-colors">Terms</a>
            <a href="#" className="hover:text-primary transition-colors">Contact</a>
          </div>
        </div>
      </footer>

      <style>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px) rotate(-0.5deg); }
          50% { transform: translateY(-15px) rotate(0.5deg); }
        }
        @keyframes float-delayed {
          0%, 100% { transform: translateY(0px) rotate(1deg); }
          50% { transform: translateY(-12px) rotate(-1deg); }
        }
        @keyframes float-slow {
          0%, 100% { transform: translateX(0px); }
          50% { transform: translateX(-8px); }
        }
        @keyframes scan-move {
          0% { top: 0%; opacity: 0.4; }
          50% { opacity: 1; }
          100% { top: 100%; opacity: 0.4; }
        }
        .animate-float { animation: float 6s ease-in-out infinite; }
        .animate-float-delayed { animation: float-delayed 8s ease-in-out infinite; }
        .animate-float-slow { animation: float-slow 10s ease-in-out infinite; }
        .animate-scan-move { animation: scan-move 3.5s ease-in-out infinite; }
      `}</style>
    </div>
  );
};

export default Index;