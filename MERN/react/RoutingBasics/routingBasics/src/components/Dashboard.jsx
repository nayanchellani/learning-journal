// Dashboard.jsx
function Dashboard() {
  return (
    <div style={{
      display: "flex",
      minHeight: "100vh",
      backgroundColor: "#f4f6f9",
      fontFamily: "Arial, sans-serif"
    }}>
      
      {/* Sidebar */}
      <aside style={{
        width: "250px",
        background: "#2c3e50",
        color: "#ecf0f1",
        padding: "20px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between"
      }}>
        <div>
          <h2 style={{ textAlign: "center", marginBottom: "30px" }}>📊 Dashboard</h2>
          <nav style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
            <a href="#" style={{ color: "#ecf0f1", textDecoration: "none" }}>🏠 Home</a>
            <a href="#" style={{ color: "#ecf0f1", textDecoration: "none" }}>📈 Analytics</a>
            <a href="#" style={{ color: "#ecf0f1", textDecoration: "none" }}>👤 Profile</a>
            <a href="#" style={{ color: "#ecf0f1", textDecoration: "none" }}>⚙️ Settings</a>
          </nav>
        </div>
        <button style={{
          background: "#e74c3c",
          border: "none",
          padding: "10px",
          color: "#fff",
          borderRadius: "5px",
          cursor: "pointer"
        }}>
          Logout
        </button>
      </aside>

      {/* Main Content */}
      <main style={{ flex: 1, padding: "30px" }}>
        <header style={{ marginBottom: "20px" }}>
          <h1 style={{ margin: 0 }}>Welcome back, Nayan 👋</h1>
          <p>Here’s a quick overview of your activity today.</p>
        </header>

        {/* Stats Section */}
        <section style={{ 
          display: "grid", 
          gridTemplateColumns: "repeat(3, 1fr)", 
          gap: "20px" 
        }}>
          <div style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
          }}>
            <h3>New Users</h3>
            <p style={{ fontSize: "1.5rem", fontWeight: "bold" }}>120</p>
          </div>
          <div style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
          }}>
            <h3>Revenue</h3>
            <p style={{ fontSize: "1.5rem", fontWeight: "bold" }}>$5,400</p>
          </div>
          <div style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
          }}>
            <h3>Orders</h3>
            <p style={{ fontSize: "1.5rem", fontWeight: "bold" }}>89</p>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Dashboard;
