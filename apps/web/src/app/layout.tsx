/* Use case: Defines the shared document shell for every ExecPlus page.
What it does: Applies global styling, metadata, and the root HTML structure. */

import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";

export const metadata: Metadata = {
  title: "ExecPlus",
  description: "Verified conversational analytics for structured business data",
};

type RootLayoutProps = Readonly<{
  children: ReactNode;
}>;

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

