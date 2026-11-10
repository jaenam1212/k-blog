'use client';

interface AdSenseSlotProps {
  slotId?: string;
  format?: 'auto' | 'fluid' | 'rectangle';
  className?: string;
}

export function AdSenseSlot({
  slotId = '1234567890',
  format = 'auto',
  className = '',
}: AdSenseSlotProps) {
  // In production, replace with actual Google AdSense client ID
  const isDev = process.env.NODE_ENV !== 'production';

  return (
    <aside
      className={`my-8 p-4 bg-neutral-50 dark:bg-neutral-900 border border-dashed border-neutral-300 dark:border-neutral-800 rounded-xl text-center text-xs text-neutral-400 ${className}`}
      aria-label="Sponsored Advertisement"
    >
      <div className="text-[10px] uppercase font-mono tracking-wider mb-2 text-neutral-400">
        SPONSORED ADVERTISEMENT
      </div>
      <div className="min-h-[100px] flex items-center justify-center font-mono bg-neutral-100 dark:bg-neutral-800/50 rounded-lg p-4">
        {isDev ? (
          <span>[Google AdSense Responsive Slot: {slotId} ({format})]</span>
        ) : (
          <ins
            className="adsbygoogle"
            style={{ display: 'block' }}
            data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
            data-ad-slot={slotId}
            data-ad-format={format}
            data-full-width-responsive="true"
          />
        )}
      </div>
    </aside>
  );
}
