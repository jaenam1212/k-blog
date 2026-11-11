export function GET() {
  return new Response('google.com, pub-9313918070358284, DIRECT, f08c47fec0942fa0\n', {
    headers: {
      'content-type': 'text/plain',
    },
  });
}
