"use client";

import { FormEvent, useState } from "react";

async function registerRequest(email: string, password: string) {
  const res = await fetch("http://localhost:8000/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) {
    const data = await res.json().catch(() => null);
    throw new Error(data?.detail ?? "Registration failed");
  }

  return res.json();
}

export default function SignupPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setMessage(null);
    setLoading(true);

    try {
      const data = await registerRequest(email, password);
      setMessage(`Welcome, ${data.email}! Your account has been created.`);
    } catch (err: any) {
      setError(err?.message ?? "Could not register. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto flex min-h-[calc(100vh-4rem)] max-w-3xl items-center justify-center px-6 py-12 text-slate-50">
      <div className="w-full rounded-2xl border border-slate-800 bg-slate-950/80 p-6 shadow-xl">
        <h1 className="text-2xl font-semibold tracking-tight">
          Join the community
        </h1>
        <p className="mt-2 text-xs text-slate-300">
          Create an account to save local-language journeys, bookmark impact
          stories, and experiment with AI tools for your community.
        </p>

        <form onSubmit={handleSubmit} className="mt-6 space-y-4 text-sm">
          <div className="space-y-1">
            <label className="text-xs text-slate-200" htmlFor="email">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2 text-xs text-slate-50 outline-none ring-emerald-400/0 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-400/40"
              placeholder="you@example.org"
              required
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs text-slate-200" htmlFor="password">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2 text-xs text-slate-50 outline-none ring-emerald-400/0 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-400/40"
              placeholder="Create a password"
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="mt-2 inline-flex w-full items-center justify-center rounded-full bg-emerald-400 px-4 py-2 text-xs font-medium text-slate-950 hover:bg-emerald-300 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Creating your account..." : "Sign up"}
          </button>
        </form>

        {error && (
          <p className="mt-4 rounded-xl border border-red-500/40 bg-red-950/40 p-3 text-[11px] text-red-100">
            {error}
          </p>
        )}

        {message && (
          <p className="mt-4 rounded-xl border border-emerald-500/40 bg-emerald-950/40 p-3 text-[11px] text-emerald-100">
            {message}
          </p>
        )}
      </div>
    </div>
  );
}

