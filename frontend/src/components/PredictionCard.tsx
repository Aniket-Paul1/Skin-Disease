import React from 'react';
import {
  AlertTriangle,
  CheckCircle,
  Info,
  ChevronRight,
  Stethoscope,
} from 'lucide-react';
import { PredictionResult } from '@/types';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import { CONDITION_INFO } from "@/data/conditionInfo";

interface PredictionCardProps {
  prediction: PredictionResult;
  onShowHospitals: () => void;
}

const PredictionCard: React.FC<PredictionCardProps> = ({
  prediction,
  onShowHospitals,
}) => {
  const severityConfig = {
    mild: {
      icon: Info,
      color: 'text-primary',
      bgColor: 'bg-primary/10',
      borderColor: 'border-primary/30',
      label: 'Mild',
    },
    moderate: {
      icon: AlertTriangle,
      color: 'text-orange-500',
      bgColor: 'bg-orange-50',
      borderColor: 'border-orange-200',
      label: 'Moderate',
    },
    severe: {
      icon: AlertTriangle,
      color: 'text-destructive',
      bgColor: 'bg-destructive/10',
      borderColor: 'border-destructive/30',
      label: 'Severe',
    },
  };

  const severityKey =
    (prediction.severity?.toLowerCase() as keyof typeof severityConfig) ||
    'mild';

  const severity = severityConfig[severityKey] || severityConfig.mild;
  const SeverityIcon = severity.icon;
  const conditionKey = prediction.disease
    ?.toLowerCase()
    .replace(/\(.*?\)/g, "")   // remove (onychomycosis)
    .replace(/'/g, "")         // remove apostrophes
    .replace(/[^a-z\s]/g, "")  // remove special chars
    .trim()
    .replace(/\s+/g, "_");     // spaces → underscores

  const conditionInfo = conditionKey
    ? CONDITION_INFO[conditionKey]
    : null;



  return (
    <div className="bg-card rounded-2xl shadow-card border border-border overflow-hidden animate-scale-in">
      {/* Header */}
      <div
        className={cn(
          'p-6 border-b',
          severity.bgColor,
          severity.borderColor
        )}
      >
        <div className="flex items-start gap-3">
          <div className="p-2 rounded-xl bg-white/50 shadow-sm">
            <SeverityIcon className={cn('w-6 h-6', severity.color)} />
          </div>
          <div>
            <h3 className="text-xl font-bold text-foreground">
              {prediction.disease}
            </h3>
            <div className="flex items-center gap-2 mt-1">
              <span className={cn('text-sm font-medium', severity.color)}>
                {severity.label} Severity
              </span>
              <span className="text-muted-foreground">•</span>
              <span className="text-sm text-muted-foreground">
                {prediction.confidence.toFixed(1)}% confidence
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Body */}
      <div className="p-6 space-y-6">
        {prediction.recommendations &&
          prediction.recommendations.length > 0 && (
            <div>
              <h4 className="text-sm font-semibold mb-3 uppercase tracking-wide">
                Recommendations
              </h4>
              <ul className="space-y-2">
                {prediction.recommendations.map((rec, index) => (
                  <li key={index} className="flex items-start gap-3">
                    <CheckCircle className="w-5 h-5 text-emerald-500 mt-0.5" />
                    <span className="text-muted-foreground">{rec}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        {/* ABOUT THE CONDITION */}
        {conditionInfo && (
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 space-y-3">
            <h4 className="font-bold text-slate-900">
              About {conditionInfo.title}
            </h4>

            <p className="text-sm text-slate-600">
              {conditionInfo.description}
            </p>

            <div>
              <p className="text-xs font-bold text-slate-500 uppercase">
                Common Causes
              </p>
              <ul className="list-disc list-inside text-sm text-slate-600">
                {conditionInfo.causes.map((cause, i) => (
                  <li key={i}>{cause}</li>
                ))}
              </ul>
            </div>

            <div>
              <p className="text-xs font-bold text-slate-500 uppercase">
                General Care & Remedies
              </p>
              <ul className="list-disc list-inside text-sm text-slate-600">
                {conditionInfo.remedies.map((remedy, i) => (
                  <li key={i}>{remedy}</li>
                ))}
              </ul>
            </div>

            <p className="text-xs text-slate-500 italic">
              {conditionInfo.note}
            </p>
          </div>
        )}

        <Button
          onClick={onShowHospitals}
          variant="default"
          size="lg"
          className="w-full gap-2 font-bold"
        >
          <Stethoscope className="w-5 h-5" />
          Find Nearby Hospitals
          <ChevronRight className="w-4 h-4" />
        </Button>
      </div>
    </div>
  );
};

export default PredictionCard;
