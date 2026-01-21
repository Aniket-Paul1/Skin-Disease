export interface PredictionResult {
  id: string;
  imageUrl: string;
  disease: string;
  confidence: number;
  severity: 'mild' | 'moderate' | 'severe';
  description: string;
  recommendations: string[];
  createdAt: Date;
}

export interface Doctor {
  id: string;
  name: string;
  specialty: string;
  hospital: string;
  rating: number;
  reviewCount: number;
  address: string;
  phone: string;
  availableSlots: string[];
  imageUrl: string;
}

export interface Hospital {
  id: string;
  name: string;
  address: string;
  phone: string;
  rating: number;
  specialties: string[];
  distance: string;
}

export interface HistoryItem extends PredictionResult {
  location: {
    city: string;
    state: string;
  };
}
