/**
 * Headers for plain REST calls to Supabase/PostgREST.
 *
 * Legacy `anon` / `service_role` keys are JWTs and ride on the Authorization
 * header. The new publishable (`sb_publishable_…`) and secret (`sb_secret_…`)
 * keys are not JWTs and must be sent on `apikey` only: sending them on
 * Authorization makes the platform reject the request with "Invalid JWT".
 * @see https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys
 */
export function supabaseAuthHeaders(key: string, extra?: Record<string, string>): Record<string, string> {
  const headers: Record<string, string> = { apikey: key, ...extra };
  if (key.startsWith('eyJ')) {
    headers.Authorization = `Bearer ${key}`;
  }
  return headers;
}
