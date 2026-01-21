import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useJsApiLoader } from '@react-google-maps/api';
import {
  History,
  LogOut,
  User,
  X,
  LayoutDashboard,
  MapPin,
  Loader2,
  Mail,
  ShieldCheck,
  CircleUser,
  Printer
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import Logo from '@/components/Logo';
import ImageUpload from '@/components/ImageUpload';
import PredictionCard from '@/components/PredictionCard';
import { DoctorCard } from '@/components/DoctorCard';
import HistoryList from '@/components/HistoryList';
import { useAuth } from '@/contexts/AuthContext';
import { supabase } from '@/lib/supabase';
import { PredictionResult } from '@/types';
import { useToast } from '@/hooks/use-toast';
import { cn } from '@/lib/utils';

type Tab = 'analyze' | 'history' | 'profile';
type ResultView = 'doctors' | 'hospitals';

const libraries: ("places")[] = ["places"];

const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const { toast } = useToast();


  const [activeTab, setActiveTab] = useState<Tab>('analyze');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [isLocating, setIsLocating] = useState(false);
  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [showRecommendations, setShowRecommendations] = useState(false);
  const [history, setHistory] = useState<any[]>([]);
  const [realHospitals, setRealHospitals] = useState<any[]>([]);
  const [city, setCity] = useState(user?.user_metadata?.city || "");
  const [stateName, setStateName] = useState(user?.user_metadata?.state || "");
  const [savingLocation, setSavingLocation] = useState(false);
  const [states, setStates] = useState<string[]>([]);
  const [cities, setCities] = useState<string[]>([]);
  const isLocationFilled = city.trim() !== "" && stateName.trim() !== "";
  const [locationSaved, setLocationSaved] = useState(false);
  const [useLiveLocation, setUseLiveLocation] = useState(false);






  const fetchHistory = async () => {
    if (!user) return;
    const { data, error } = await supabase
      .from('scans')
      .select('*')
      .eq('user_id', user.id)
      .order('created_at', { ascending: false });

    if (!error) setHistory(data || []);
  };

  const fetchHospitalsByLiveLocation = async () => {
    if (!navigator.geolocation) {
      toast({
        variant: "destructive",
        title: "Location not supported",
        description: "Your browser does not support location access.",
      });
      return;
    }

    setIsLocating(true);

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        try {
          const { latitude, longitude } = position.coords;

          const res = await fetch(
            `http://127.0.0.1:8000/verified-doctors?lat=${latitude}&lng=${longitude}`
          );

          const data = await res.json();
          setRealHospitals(data);
          setShowRecommendations(true);
        } catch (err) {
          toast({
            variant: "destructive",
            title: "Failed to fetch hospitals",
            description: "Unable to load nearby hospitals.",
          });
        } finally {
          setIsLocating(false);
        }
      },
      () => {
        setIsLocating(false);
        toast({
          variant: "destructive",
          title: "Location permission denied",
          description: "Please allow location access or save your city and state.",
        });
      }
    );
  };


  const fetchHospitals = async () => {
    // ✅ Case 1: Saved location exists
    if (city && stateName) {
      try {
        setIsLocating(true);

        const res = await fetch(
          `http://127.0.0.1:8000/verified-doctors?city=${encodeURIComponent(
            city
          )}&state=${encodeURIComponent(stateName)}`
        );

        const data = await res.json();
        setRealHospitals(data);
        setShowRecommendations(true);
      } catch (err) {
        console.error("Hospital fetch failed", err);
      } finally {
        setIsLocating(false);
      }
      return;
    }

    // ✅ Case 2: No saved location → use live location
    fetchHospitalsByLiveLocation();
  };



  useEffect(() => {
    if (user) fetchHistory();
    else navigate('/login');
  }, [user, navigate]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/locations/states")
      .then(res => res.json())
      .then(data => setStates(data))
      .catch(err => console.error("Failed to load states", err));
  }, []);



  useEffect(() => {
    if (!stateName) {
      setCities([]);
      setCity("");
      return;
    }

    fetch(
      `http://127.0.0.1:8000/locations/cities?state=${encodeURIComponent(stateName)}`
    )
      .then(res => res.json())
      .then(data => setCities(data))
      .catch(err => console.error("Failed to load cities", err));
  }, [stateName]);

  useEffect(() => {
    setLocationSaved(false);
  }, [city, stateName]);




  const handlePrintSingle = (item: any) => {
    const printWindow = window.open('', '_blank');
    if (!printWindow) return;

    const content = `
      <html>
        <head>
          <title>Analysis Report - ${item.disease}</title>
          <style>
            body { font-family: sans-serif; padding: 40px; color: #333; line-height: 1.6; }
            .header { border-bottom: 2px solid #2563eb; padding-bottom: 15px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-end; }
            .patient-box { background: #f1f5f9; padding: 20px; border-radius: 12px; margin-bottom: 30px; }
            .result-container { display: flex; gap: 30px; margin-top: 20px; }
            .scan-image { width: 300px; height: 300px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; }
            .details { flex: 1; }
            .disease-title { font-size: 24px; font-weight: bold; color: #1e293b; margin: 0; }
            .confidence-badge { display: inline-block; padding: 4px 12px; background: #dcfce7; color: #166534; border-radius: 20px; font-weight: bold; font-size: 14px; margin: 10px 0; }
            .description-box { margin-top: 20px; padding: 15px; border-left: 4px solid #cbd5e1; }
            .footer { margin-top: 50px; font-size: 11px; color: #64748b; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 20px; }
            @media print { .no-print { display: none; } }
          </style>
        </head>
        <body>
          <div class="header">
            <div>
              <h1 style="margin:0; color:#2563eb;">DermaCare AI</h1>
              <p style="margin:0; color:#64748b;">Clinical Analysis Report</p>
            </div>
            <div style="text-align:right">
              <p style="margin:0;"><strong>Date:</strong> ${new Date(item.created_at || Date.now()).toLocaleDateString()}</p>
            </div>
          </div>

          <div class="patient-box">
            <h3 style="margin-top:0">Patient Information</h3>
            <p style="margin:4px 0;"><strong>Name:</strong> ${user?.user_metadata?.full_name || 'Patient'}</p>
            <p style="margin:4px 0;"><strong>Email:</strong> ${user?.email}</p>
          </div>

          <div class="result-container">
            ${item.imageUrl ? `<img src="${item.imageUrl}" class="scan-image" />` : ''}
            <div class="details">
              <p style="text-transform:uppercase; font-size:12px; font-weight:bold; color:#64748b; margin-bottom:5px;">Detected Condition</p>
              <h2 class="disease-title">${item.disease}</h2>
              <div class="confidence-badge">AI Confidence: ${item.confidence.toFixed(1)}%</div>
            </div>
          </div>

          <div class="footer">
            <p><strong>Disclaimer:</strong> This report is generated by an artificial intelligence system and is intended for informational purposes only. It does not constitute a formal medical diagnosis. Please present this report to a licensed dermatologist for professional evaluation.</p>
          </div>
          <script>window.onload = () => { window.print(); setTimeout(() => { window.close(); }, 500); }</script>
        </body>
      </html>
    `;

    printWindow.document.write(content);
    printWindow.document.close();
  };

  const handlePrintHistory = () => {
    const printWindow = window.open('', '_blank');
    if (!printWindow) return;

    const content = `
      <html>
        <head>
          <title>Medical History Report - ${user?.user_metadata?.full_name || 'User'}</title>
          <style>
            body { font-family: sans-serif; padding: 40px; color: #333; }
            h1 { color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
            .user-info { margin-bottom: 30px; background: #f8fafc; padding: 15px; border-radius: 8px; }
            .scan-card { border: 1px solid #e2e8f0; padding: 20px; margin-bottom: 20px; border-radius: 12px; page-break-inside: avoid; }
            .scan-header { display: flex; justify-content: space-between; margin-bottom: 10px; }
            .disease { font-size: 18px; font-weight: bold; color: #2563eb; }
            .date { color: #64748b; font-size: 14px; }
            .confidence { color: #059669; font-weight: 600; font-size: 14px; }
            .description { margin-top: 10px; line-height: 1.5; color: #475569; }
            .footer { margin-top: 50px; font-size: 12px; color: #94a3b8; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 20px; }
          </style>
        </head>
        <body>
          <h1>DermaCare AI</h1>
          <h3>Skin Analysis Medical History</h3>
          <div class="user-info">
            <p><strong>Patient Name:</strong> ${user?.user_metadata?.full_name || 'N/A'}</p>
            <p><strong>Email:</strong> ${user?.email}</p>
            <p><strong>Report Generated:</strong> ${new Date().toLocaleString()}</p>
          </div>
          ${history.map(item => `
            <div class="scan-card">
              <div class="scan-header">
                <span class="disease">${item.disease}</span>
                <span class="date">${new Date(item.created_at).toLocaleDateString()}</span>
              </div>
              <div class="confidence">AI Confidence: ${item.confidence.toFixed(1)}%</div>
            </div>
          `).join('')}
          <div class="footer">
            This is an AI-generated summary report. Please consult a professional dermatologist for clinical diagnosis.
          </div>
          <script>window.onload = () => { window.print(); window.close(); }</script>
        </body>
      </html>
    `;

    printWindow.document.write(content);
    printWindow.document.close();
  };




  const handleImageSelect = async (file: File) => {
    if (!user) return;

    setIsAnalyzing(true);
    setPrediction(null);
    setShowRecommendations(false);

    try {
      const ext = file.name.split('.').pop();
      const filePath = `${user.id}/${Date.now()}.${ext}`;

      // 1️⃣ Upload image to Supabase
      const { error: uploadError } = await supabase
        .storage
        .from('skin-images')
        .upload(filePath, file);

      if (uploadError) throw uploadError;

      const { data: { publicUrl } } = supabase
        .storage
        .from('skin-images')
        .getPublicUrl(filePath);

      // 2️⃣ CALL REAL ML BACKEND (REPLACED DUMMY CODE)
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/predict`, {
        method: "POST",
        body: formData
      });

      if (!response.ok) {
        throw new Error("AI prediction failed");
      }

      const ai = await response.json();

      const aiResult: PredictionResult = {
        disease: ai.disease,
        confidence: ai.confidence, // already %
        description: ai.description,
        imageUrl: publicUrl
      };

      // 3️⃣ Save result
      await supabase.from('scans').insert([{
        user_id: user.id,
        image_url: publicUrl,
        disease: aiResult.disease,
        confidence: aiResult.confidence,
        description: aiResult.description
      }]);

      setPrediction(aiResult);
      fetchHistory();

      toast({
        title: "Analysis Complete",
        description: "AI prediction generated successfully."
      });

    } catch (err: any) {
      toast({
        variant: "destructive",
        title: "Prediction Error",
        description: err.message || "Something went wrong"
      });
    } finally {
      setIsAnalyzing(false);
    }
  };
  
  const handleShowHospitals = () => {
    // If location is saved → use saved location
    if (city && stateName) {
      fetchHospitals();
      return;
    }

    // If user explicitly chose live location
    if (useLiveLocation) {
      fetchHospitalsByLiveLocation();
      return;
    }

    // Otherwise → ask user to choose
    toast({
      title: "Location required",
      description: "Please save your city & state or use your current location.",
    });
  };


  const handleSaveLocation = async () => {
    if (!city.trim() || !stateName.trim()) {
      toast({
        variant: "destructive",
        title: "Missing information",
        description: "Please enter both city and state.",
      });
      return;
    }

    try {
      setSavingLocation(true);

      const { error } = await supabase.auth.updateUser({
        data: {
          city: city.trim(),
          state: stateName.trim(),
        },
      });

      if (error) throw error;

      toast({
        title: "Location updated",
        description: "Your location has been saved successfully.",
      });

      // ✅ Mark location as saved (used to hide Save button)
      setLocationSaved(true);

      // ✅ Automatically refresh hospitals for new location
      await fetchHospitals();

    } catch (err: any) {
      toast({
        variant: "destructive",
        title: "Update failed",
        description: err.message,
      });
    } finally {
      setSavingLocation(false);
    }
  };



  return (
    <div className="flex min-h-screen bg-[#FDFDFF]">
      <aside className="w-64 bg-slate-50/50 border-r border-slate-100 flex flex-col sticky top-0 h-screen">
        <div className="p-8"><Logo /></div>
        <nav className="flex-1 px-4 space-y-2">
          <button onClick={() => setActiveTab('analyze')} className={cn("w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold", activeTab === 'analyze' ? "bg-primary/10 text-primary" : "text-slate-500 hover:bg-slate-50")}>
            <LayoutDashboard className="w-5 h-5" /> Analyze Skin
          </button>
          <button onClick={() => setActiveTab('history')} className={cn("w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold", activeTab === 'history' ? "bg-primary/10 text-primary" : "text-slate-500 hover:bg-slate-50")}>
            <History className="w-5 h-5" /> History
            {history.length > 0 && <span className="ml-auto bg-primary text-white text-[10px] px-2 py-0.5 rounded-full">{history.length}</span>}
          </button>
          <button onClick={() => setActiveTab('profile')} className={cn("w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold", activeTab === 'profile' ? "bg-primary/10 text-primary" : "text-slate-500 hover:bg-slate-50")}>
            <User className="w-5 h-5" /> Profile
          </button>
        </nav>
        <div className="p-4 border-t border-slate-100">
          <Button variant="ghost" className="w-full justify-start gap-3 text-red-500 hover:bg-red-50 rounded-xl" onClick={async () => { await supabase.auth.signOut(); navigate('/'); }}><LogOut className="w-4 h-4" /> Sign Out</Button>
        </div>
      </aside>

      <main className="flex-1 p-10 overflow-y-auto">
        <div className="max-w-5xl mx-auto">
          {activeTab === 'analyze' && (
            <div className="space-y-8 animate-slide-up">
              <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
                <header className="mb-8">
                  <h1 className="text-2xl font-bold text-slate-900">Skin Analysis</h1>
                  <p className="text-slate-500 text-sm">Upload a photo to detect conditions and find nearby specialists.</p>
                </header>
                <ImageUpload onImageSelect={handleImageSelect} isAnalyzing={isAnalyzing} />
              </div>
              {!prediction && !isAnalyzing && !showRecommendations && (
                <div className="bg-white rounded-3xl p-8 border border-slate-100 text-center">
                  <p className="text-slate-600 font-medium">
                    Upload Image to Analyze.
                  </p>
                </div>
              )}

              {prediction && !showRecommendations && (
                <div className="relative">
                  <div className="absolute top-4 right-4 z-10 flex gap-2">
                    <button 
                      onClick={() => handlePrintSingle(prediction)} 
                      className="p-2 bg-white border border-slate-200 shadow-sm rounded-full hover:bg-slate-50 text-slate-600"
                      title="Print Report"
                    >
                      <Printer className="w-4 h-4" />
                    </button>
                    <button onClick={() => setPrediction(null)} className="p-2 bg-slate-100 rounded-full hover:bg-slate-200">
                      <X className="w-4 h-4" />
                    </button>
                  </div>
                  <PredictionCard prediction={prediction} onShowHospitals={handleShowHospitals} />
                  {isLocating && (
                    <div className="absolute inset-0 bg-white/60 backdrop-blur-sm flex items-center justify-center rounded-3xl z-20">
                      <div className="flex flex-col items-center gap-3">
                        <Loader2 className="w-8 h-8 animate-spin text-primary" />
                        <p className="font-bold text-slate-700">Locating specialists...</p>
                      </div>
                    </div>
                  )}
                </div>
              )}
              
              {/* Use Live Location (only if no saved location) */}
              {prediction && !showRecommendations && !city && !stateName && (
                <div className="bg-white rounded-2xl p-4 border border-slate-100 text-center">
                  <p className="text-sm text-slate-600 mb-3">
                    You have not saved your location yet.
                  </p>
                  <Button
                    variant="outline"
                    className="w-full font-bold"
                    onClick={() => {
                      setUseLiveLocation(true);
                      fetchHospitalsByLiveLocation();
                    }}
                  >
                    Use my current location
                  </Button>
                </div>
              )}

              {/* Location Preferences */}
              <div className="pt-6 space-y-4">
                <h3 className="text-sm font-bold text-slate-900 uppercase tracking-wide">
                  Location Preferences
                </h3>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-1">
                    <p className="text-[10px] uppercase font-bold text-slate-400">
                      City
                    </p>
                    <select
                      value={city}
                      onChange={(e) => setCity(e.target.value)}
                      disabled={!stateName}
                      className="w-full px-4 py-2 rounded-xl border border-slate-200 bg-white disabled:bg-slate-100 disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-primary/20"
                    >
                      <option value="">
                        {stateName ? "Select City" : "Select State First"}
                      </option>
                      {cities.map((c) => (
                        <option key={c} value={c}>
                          {c}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="space-y-1">
                    <p className="text-[10px] uppercase font-bold text-slate-400">
                     State
                    </p>
                   <select
                      value={stateName}
                      onChange={(e) => {
                        setStateName(e.target.value);
                        setCity(""); // reset city when state changes
                      }}
                      className="w-full px-4 py-2 rounded-xl border border-slate-200 bg-white focus:outline-none focus:ring-2 focus:ring-primary/20"
                    >
                      <option value="">Select State</option>
                      {states.map((s) => (
                        <option key={s} value={s}>
                          {s}
                        </option>
                      ))}
                    </select>
                  </div>
                </div>

                {isLocationFilled && !locationSaved && (
                  <Button
                    onClick={handleSaveLocation}
                    disabled={savingLocation}
                    className="mt-4 w-full font-bold rounded-xl"
                  >
                    {savingLocation ? "Saving..." : "Save Location"}
                  </Button>
                )}
                {locationSaved && (
                  <p className="text-sm text-green-600 font-semibold mt-3">
                    Location saved successfully
                  </p>
                )}

              </div>

              {showRecommendations && (
                <div className="space-y-6 animate-slide-up">
                  <div className="flex items-center justify-between">
                    <h2 className="text-xl font-bold text-slate-900">Nearby Support</h2>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setShowRecommendations(false)}
                    >
                      <X className="w-4 h-4 mr-2" />
                      Close
                    </Button>
                  </div>

                  <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {realHospitals.length === 0 ? (
                      <div className="col-span-full text-center py-10 text-slate-500">
                        <p className="font-bold">No hospitals found</p>
                        <p className="text-sm">
                          Please allow location access or try again later.
                        </p>
                     </div>
                    ) : (
                      realHospitals.map((h, index) => (
                        <div
                          key={index}
                          className="bg-white p-5 rounded-2xl border border-slate-100 shadow-sm space-y-3 hover:shadow-md transition"
                        >
                          <h4 className="font-bold text-slate-900 leading-tight line-clamp-2">
                            {h.name}
                          </h4>

                          <p className="text-xs text-slate-500 italic line-clamp-2">
                            {h.address}
                          </p>

                          <div className="flex items-center justify-between text-xs mt-2">
                            <span className="text-orange-500 font-bold">
                              ⭐ {h.rating ?? "N/A"}
                            </span>

                            {h.open_now !== undefined && (
                              <span
                                className={`font-bold ${
                                  h.open_now ? "text-green-600" : "text-red-500"
                                }`}
                              >
                                {h.open_now ? "Open Now" : "Closed"}
                              </span>
                            )}
                          </div>

                          <Button
                            className="w-full gap-2 font-bold rounded-xl"
                            variant="outline"
                            onClick={() => {
                              if (h.map_url) {
                                window.open(h.map_url, "_blank", "noopener,noreferrer");
                              } else {
                                alert("Map location not available");
                              }
                            }}
                          >
                            <MapPin className="w-4 h-4" />
                            Navigate
                          </Button>
                        </div>
                      ))
                    )}
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'history' && (
            <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm animate-slide-up">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-slate-900">Medical History</h2>
                <Button 
                  onClick={handlePrintHistory}
                  variant="outline" 
                  className="gap-2 rounded-xl"
                  disabled={history.length === 0}
                >
                  <Printer className="w-4 h-4" /> Print Full History
                </Button>
              </div>
              <HistoryList items={history} onSelectItem={(item) => {
                setPrediction({ ...item, imageUrl: item.image_url } as any);
                setActiveTab('analyze');
              }} onDeleteSuccess={fetchHistory} />
            </div>
          )}

          {activeTab === 'profile' && (
            <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm animate-slide-up">
              <h2 className="text-2xl font-bold text-slate-900 mb-8">User Profile</h2>
              <div className="space-y-6 max-w-lg">
                <div className="flex items-center gap-4 p-4 bg-slate-50 rounded-2xl border border-slate-100">
                  <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center text-primary">
                    <User className="w-8 h-8" />
                  </div>
                  <div>
                    <h3 className="font-bold text-slate-900 text-lg">Account Details</h3>
                    <p className="text-slate-500 text-sm">Manage your personal information</p>
                  </div>
                </div>
                
                <div className="space-y-4">
                  <div className="flex items-center gap-3 px-4 py-3 bg-white border border-slate-100 rounded-xl">
                    <CircleUser className="w-5 h-5 text-slate-400" />
                    <div className="flex-1">
                      <p className="text-[10px] uppercase font-bold text-slate-400">Full Name</p>
                      <p className="text-slate-700 font-medium">{user?.user_metadata?.full_name || 'Patient User'}</p>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 px-4 py-3 bg-white border border-slate-100 rounded-xl">
                    <Mail className="w-5 h-5 text-slate-400" />
                    <div className="flex-1">
                      <p className="text-[10px] uppercase font-bold text-slate-400">Email Address</p>
                      <p className="text-slate-700 font-medium">{user?.email}</p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-3 px-4 py-3 bg-white border border-slate-100 rounded-xl">
                    <ShieldCheck className="w-5 h-5 text-slate-400" />
                    <div className="flex-1">
                      <p className="text-[10px] uppercase font-bold text-slate-400">User ID</p>
                      <p className="text-slate-700 font-mono text-sm">{user?.id}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default Dashboard;