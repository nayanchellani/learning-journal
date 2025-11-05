// Home.jsx
function Home() {
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      height: "100vh",
      background: "linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%)",
      color: "#fff",
      fontFamily: "Arial, sans-serif",
      textAlign: "center"
    }}>
      <h1 style={{ fontSize: "3rem", marginBottom: "20px" }}>
        🏠 Welcome to the Home Page
      </h1>
      <p style={{ fontSize: "1.25rem", maxWidth: "600px" }}>
        This is the starting point of our React app.  
        Navigate through the menu to explore different pages.
      </p>
      <button style={{
        marginTop: "30px",
        padding: "10px 20px",
        fontSize: "1rem",
        border: "none",
        borderRadius: "8px",
        backgroundColor: "#ff6b6b",
        color: "#fff",
        cursor: "pointer",
        transition: "background 0.3s"
      }}
      onMouseOver={(e) => e.target.style.backgroundColor = "#ff4757"}
      onMouseOut={(e) => e.target.style.backgroundColor = "#ff6b6b"}>
        Get Started 🚀
      </button>
    </div>
  );
}

export default Home;
