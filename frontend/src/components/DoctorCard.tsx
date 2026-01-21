import React from 'react';
import { Star, Phone, MapPin, Clock, ChevronRight } from 'lucide-react';
import { Doctor, Hospital } from '@/types';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

interface DoctorCardProps {
  doctor: Doctor;
}

export const DoctorCard: React.FC<DoctorCardProps> = ({ doctor }) => {
  return (
    <div className="bg-card rounded-xl shadow-card border border-border p-5 hover:shadow-card-hover transition-all duration-300">
      <div className="flex gap-4">
        <img 
          src={doctor.imageUrl} 
          alt={doctor.name}
          className="w-20 h-20 rounded-xl object-cover"
        />
        <div className="flex-1 min-w-0">
          <h4 className="font-semibold text-foreground truncate">{doctor.name}</h4>
          <p className="text-sm text-muted-foreground truncate">{doctor.specialty}</p>
          <p className="text-sm text-primary truncate">{doctor.hospital}</p>
          <div className="flex items-center gap-1 mt-2">
            <Star className="w-4 h-4 text-warning fill-warning" />
            <span className="text-sm font-medium text-foreground">{doctor.rating}</span>
            <span className="text-sm text-muted-foreground">({doctor.reviewCount} reviews)</span>
          </div>
        </div>
      </div>
      
      <div className="mt-4 space-y-2">
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <MapPin className="w-4 h-4 flex-shrink-0" />
          <span className="truncate">{doctor.address}</span>
        </div>
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <Phone className="w-4 h-4 flex-shrink-0" />
          <span>{doctor.phone}</span>
        </div>
      </div>

      <div className="mt-4">
        <p className="text-xs font-medium text-foreground mb-2">Available Slots Today:</p>
        <div className="flex flex-wrap gap-2">
          {doctor.availableSlots.slice(0, 3).map((slot, index) => (
            <span 
              key={index}
              className="px-3 py-1 bg-primary/10 text-primary text-xs font-medium rounded-full"
            >
              {slot}
            </span>
          ))}
          {doctor.availableSlots.length > 3 && (
            <span className="px-3 py-1 bg-secondary text-muted-foreground text-xs font-medium rounded-full">
              +{doctor.availableSlots.length - 3} more
            </span>
          )}
        </div>
      </div>

      <Button variant="outline" size="sm" className="w-full mt-4">
        Book Appointment
        <ChevronRight className="w-4 h-4" />
      </Button>
    </div>
  );
};

interface HospitalCardProps {
  hospital: Hospital;
}

export const HospitalCard: React.FC<HospitalCardProps> = ({ hospital }) => {
  return (
    <div className="bg-card rounded-xl shadow-card border border-border p-5 hover:shadow-card-hover transition-all duration-300">
      <div className="flex items-start justify-between">
        <div>
          <h4 className="font-semibold text-foreground">{hospital.name}</h4>
          <div className="flex items-center gap-1 mt-1">
            <Star className="w-4 h-4 text-warning fill-warning" />
            <span className="text-sm font-medium text-foreground">{hospital.rating}</span>
          </div>
        </div>
        <span className="px-3 py-1 bg-primary/10 text-primary text-sm font-medium rounded-full">
          {hospital.distance}
        </span>
      </div>
      
      <div className="mt-4 space-y-2">
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <MapPin className="w-4 h-4 flex-shrink-0" />
          <span>{hospital.address}</span>
        </div>
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <Phone className="w-4 h-4 flex-shrink-0" />
          <span>{hospital.phone}</span>
        </div>
      </div>

      <div className="mt-4">
        <p className="text-xs font-medium text-foreground mb-2">Specialties:</p>
        <div className="flex flex-wrap gap-2">
          {hospital.specialties.map((specialty, index) => (
            <span 
              key={index}
              className="px-2 py-1 bg-secondary text-secondary-foreground text-xs rounded-md"
            >
              {specialty}
            </span>
          ))}
        </div>
      </div>

      <Button variant="outline" size="sm" className="w-full mt-4">
        Get Directions
        <ChevronRight className="w-4 h-4" />
      </Button>
    </div>
  );
};
