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
  const isDev = process.env.NODE_ENV !== 'production';

  return (
    <aside
      className={`my-10 p-4 border border-dashed border-zinc-200 dark:border-zinc-800 rounded-lg text-center ${className}`}
      aria-label="Advertisement"
    >
      <div className="text-[10px] uppercase font-mono tracking-wider text-zinc-400 mb-2">
        SPONSORED
      </div>
      <div className="min-h-[90px] flex items-center justify-center font-mono text-xs text-zinc-400 bg-zinc-50 dark:bg-zinc-900/50 rounded p-4">
        {isDev ? (
          <span>[AdSense Placement · {slotId}]</span>
        ) : (
          <ins
            className="adsbygoogle"
            style={{ display: 'block' }}
            data-ad-client="ca-pub-9313918070358284"
            data-ad-slot={slotId}
            data-ad-format={format}
            data-full-width-responsive="true"
          />
        )}
      </div>
    </aside>
  );
}
