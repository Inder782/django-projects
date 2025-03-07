export const ValidateUser = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) {
    console.error("User is not authenticated");
  }
  const response = await fetch("http://127.0.0.1:8000/secure", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-type": "application/json",
    },
  });

  const data = await response.json();

  if (response.ok) {
    console.log("Secure data", data);
  } else {
    console.error("Failed to fetch secure data", data);
  }
};
