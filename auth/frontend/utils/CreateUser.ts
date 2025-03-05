export const CreateUser = async (username: string, password: string) => {
  try {
      const response = await fetch("http://127.0.0.1:8000/backend/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    // Parse response JSON
    const data = await response.json();

    if (!response.ok) {
      return data.error;
    }
    window.alert("User created successfully");
    return (window.location.href = "/login");
  } catch (error) {
    console.error("Error:", error);
    window.alert("Something went wrong. Please try again.");
  }
};
