export const metadata = {
  title: "A7DO Control",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body style={{ fontFamily: "system-ui", margin: 0 }}>
        {children}
      </body>
    </html>
  );
}
