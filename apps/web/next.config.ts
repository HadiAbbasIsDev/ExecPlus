/* Use case: Configures the Next.js application runtime.
What it does: Enables strict React checks and produces a standalone deployment artifact. */

import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  reactStrictMode: true,
};

export default nextConfig;

