import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "@/lib/supabase";
import { Loader2, CheckCircle } from "lucide-react";

const AuthCallback = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const handleAuth = async () => {
      const { data, error } = await supabase.auth.getSession();

      if (error) {
        console.error("Auth callback error:", error.message);
        navigate("/login");
        return;
      }

      if (data?.session) {
        // ✅ Email confirmed successfully
        setTimeout(() => {
          navigate("/login?verified=true");
        }, 1500);
      } else {
        navigate("/login");
      }
    };

    handleAuth();
  }, [navigate]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#FDFDFF]">
      <div className="bg-white p-10 rounded-3xl border border-slate-100 shadow-sm text-center space-y-6 max-w-md">
        <CheckCircle className="w-14 h-14 text-green-600 mx-auto" />
        <h1 className="text-2xl font-bold text-slate-900">
          Email Verified Successfully
        </h1>
        <p className="text-slate-500">
          Your email has been confirmed. Redirecting you to login…
        </p>
        <Loader2 className="w-6 h-6 animate-spin mx-auto text-primary" />
      </div>
    </div>
  );
};

export default AuthCallback;
