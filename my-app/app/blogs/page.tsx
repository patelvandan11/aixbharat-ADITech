"use client";

import { useEffect, useState } from "react";

type Blog = {
  id: number;
  title: string;
  summary: string;
  tags: string[];
};

export default function BlogsPage() {
  const [blogs, setBlogs] = useState<Blog[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadBlogs() {
      try {
        setLoading(true);
        const res = await fetch("http://localhost:8000/blogs");
        if (!res.ok) {
          throw new Error("Failed to load blogs");
        }
        const data = (await res.json()) as Blog[];
        setBlogs(data);
      } catch (err) {
        setError("Could not reach the community blog API. Is the backend running?");
      } finally {
        setLoading(false);
      }
    }

    loadBlogs();
  }, []);

  return (
    <div className="mx-auto max-w-4xl px-6 py-12 text-slate-50">
      <h1 className="text-3xl font-semibold tracking-tight">Community blogs</h1>
      <p className="mt-3 text-sm text-slate-300">
        Stories, experiments, and ideas on how AI can expand access to public
        information, learning, and opportunity.
      </p>

      {loading && (
        <p className="mt-8 text-xs text-slate-400">
          Loading stories from the Python backend...
        </p>
      )}

      {error && (
        <p className="mt-8 rounded-xl border border-red-500/40 bg-red-950/40 p-3 text-xs text-red-100">
          {error}
        </p>
      )}

      <div className="mt-8 space-y-4">
        {blogs.map((blog) => (
          <article
            key={blog.id}
            className="rounded-2xl border border-slate-800 bg-slate-950/60 p-5"
          >
            <h2 className="text-lg font-semibold text-slate-50">
              {blog.title}
            </h2>
            <p className="mt-2 text-xs text-slate-300">{blog.summary}</p>
            <div className="mt-3 flex flex-wrap gap-2 text-[11px]">
              {blog.tags?.map((tag) => (
                <span
                  key={tag}
                  className="rounded-full bg-slate-900 px-2 py-0.5 text-slate-300 ring-1 ring-slate-700"
                >
                  #{tag}
                </span>
              ))}
            </div>
          </article>
        ))}

        {!loading && !error && blogs.length === 0 && (
          <p className="text-xs text-slate-400">
            No blogs yet. Seed some stories in the FastAPI backend to see them
            here.
          </p>
        )}
      </div>
    </div>
  );
}

