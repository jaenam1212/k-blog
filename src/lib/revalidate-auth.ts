import { timingSafeEqual } from 'node:crypto';

/**
 * The shared secret that guards the write-side API routes.
 *
 * It comes from the environment only. There is deliberately no fallback value:
 * this repository is public, so any default would be a published secret.
 */
export function isRevalidateSecretConfigured(): boolean {
  return Boolean(process.env.REVALIDATE_SECRET?.trim());
}

export function isValidRevalidateSecret(given: string | null | undefined): boolean {
  const expected = process.env.REVALIDATE_SECRET?.trim();
  if (!expected || !given) return false;
  const a = Buffer.from(given);
  const b = Buffer.from(expected);
  if (a.length !== b.length) return false;
  return timingSafeEqual(a, b);
}

export const SECRET_NOT_CONFIGURED_MESSAGE =
  'REVALIDATE_SECRET is not configured on the server';

export const INVALID_SECRET_MESSAGE = 'Unauthorized invalid secret';
