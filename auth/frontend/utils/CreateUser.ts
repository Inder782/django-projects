export const CreateUser = async (username: string, password: string) => {
  try {
      const response = await fetch("http://127.0.0.1:8000/backend/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
    if (!response.ok) {
        throw new Error(`Request failed with status code ${response.status}`);
      }
    
    window.alert("User created Successfully")
    window.location.href="/login"
  } catch (error) {
    console.error("Error creating user",error)
    throw error
  }
};
