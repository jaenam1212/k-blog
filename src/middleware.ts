import { NextRequest, NextResponse } from 'next/server';

// The AdSense site is registered on the root domain (k-trand.store), and the
// ads.txt crawler must receive the file itself with HTTP 200 from that root
// domain. Everything else keeps the canonical https://www.k-trand.store host.
export function middleware(req: NextRequest) {
  const host = (req.headers.get('host') || '').split(':')[0];
  const { pathname, search } = req.nextUrl;

  if (host === 'k-trand.store') {
    if (pathname === '/ads.txt') {
      return NextResponse.next();
    }
    return NextResponse.redirect(
      new URL(`https://www.k-trand.store${pathname}${search}`),
      308
    );
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
