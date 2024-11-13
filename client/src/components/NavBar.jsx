// src/components/Navbar.jsx
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { getCurrentUser, logout } from "../services/authService";

function Navbar() {
  const navigate = useNavigate();
  const user = getCurrentUser();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav style={styles.nav}>
      <h1 style={styles.logo}>E-Learn</h1>
      <ul style={styles.navLinks}>
        {!user && (
          <>
            <li>
              <Link to="/signup">Signup</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
          </>
        )}
        {user && (
          <>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
            <li>
              <button onClick={handleLogout} style={styles.logoutButton}>
                Logout
              </button>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "1rem",
    backgroundColor: "#333",
    color: "#fff",
  },
  logo: {
    fontSize: "1.5rem",
  },
  navLinks: {
    display: "flex",
    gap: "1rem",
  },
  logoutButton: {
    background: "none",
    border: "none",
    color: "#fff",
    cursor: "pointer",
    textDecoration: "underline",
  },
};

export default Navbar;
