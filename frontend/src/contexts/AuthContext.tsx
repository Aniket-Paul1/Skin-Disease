import React, { createContext, useContext, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { User } from '@supabase/supabase-js';

// 1. Updated Interface to include login
interface AuthContextType {
  user: User | null;
  loading: boolean;
  register: (name: string, email: string, pass: string) => Promise<boolean>;
  login: (email: string, pass: string) => Promise<boolean>;
}

// 2. Updated default value
const AuthContext = createContext<AuthContextType>({ 
  user: null, 
  loading: true,
  register: async () => false,
  login: async () => false 
});

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null);
      setLoading(false);
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null);
      setLoading(false);
    });

    return () => subscription.unsubscribe();
  }, []);

  // --- REGISTER FUNCTION ---
  const register = async (name: string, email: string, pass: string) => {
    try {
      const { data, error } = await supabase.auth.signUp({
        email,
        password: pass,
        options: {
          data: { full_name: name } 
        }
      });
      
      if (error) throw error;
      return !!data.user;
    } catch (error) {
      console.error("Registration error:", error);
      return false;
    }
  };

  // --- LOGIN FUNCTION ---
  const login = async (email: string, pass: string) => {
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password: pass,
      });

      if (error) throw error;
      return !!data.user;
    } catch (error) {
      console.error("Login error:", error);
      return false;
    }
  };

  return (
    // 3. Added login to the Provider value
    <AuthContext.Provider value={{ user, loading, register, login }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);