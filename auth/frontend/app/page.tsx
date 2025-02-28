"use client";

import { signIn, signOut, useSession } from "next-auth/react";

export default function LoginPage() {
  const { data: session } = useSession();
  console.log(session)
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      {session ? (
        <>
          <p>Welcome, {session.user?.name}! </p>
      
          <button onClick={() => signOut()} className="p-2 bg-red-500 text-white">
            Sign Out
          </button>
        </>
      ) : (
        <div>
          
        <button onClick={() => signIn("github")} className="p-2 bg-blue-500 text-white">
          Sign in with GitHub
        </button>
        <button onClick={()=>signIn("google")} className="p-2 bg-blue-500 text-white">Sign  with google</button>
        </div>
      )}
    </div>
  );
}
