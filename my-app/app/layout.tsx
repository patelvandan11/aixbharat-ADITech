import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AI for Communities Hub",
  description:
    "AI for Communities, Access & Public Impact – a hub to explore projects, stories, and resources that make AI work for everyone.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-slate-950 text-slate-50`}
      >
        <div className="min-h-screen flex flex-col">
          <header className="border-b border-white/10 bg-slate-950/80 backdrop-blur">
            <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
              <div className="flex items-center gap-2">
                <span className="inline-flex h-8 w-8 items-center justify-center rounded-xl bg-emerald-400 text-slate-950 text-lg font-black">
                  AI
                </span>
                <div>
                  <p className="text-sm font-semibold leading-tight">
                    AI for Communities
                  </p>
                  <p className="text-xs text-slate-400 leading-tight">
                    Access & Public Impact
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-6 text-sm">
                <a href="/" className="hover:text-emerald-300 transition-colors">
                  Home
                </a>
                <a
                  href="/about"
                  className="hover:text-emerald-300 transition-colors"
                >
                  About
                </a>
                <a
                  href="/blogs"
                  className="hover:text-emerald-300 transition-colors"
                >
                  Blogs
                </a>
                <a
                  href="/login"
                  className="hover:text-emerald-300 transition-colors"
                >
                  Log in
                </a>
                <a
                  href="/signup"
                  className="rounded-full bg-emerald-400 px-4 py-1.5 text-slate-950 font-medium hover:bg-emerald-300 transition-colors"
                >
                  Join community
                </a>
              </div>
            </nav>
          </header>
          <main className="flex-1 bg-slate-950">{children}</main>
          <footer className="border-t border-white/10 bg-slate-950/80">
            <div className="mx-auto max-w-6xl px-6 py-4 text-xs text-slate-500 flex items-center justify-between">
              <span>
                Built for{" "}
                <span className="font-semibold">
                  AI for Communities, Access & Public Impact
                </span>
              </span>
              <span>Inclusive, accessible, and community-first AI.</span>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}
