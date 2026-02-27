// main.js - handling auth state and common UI updates

document.addEventListener('DOMContentLoaded', () => {
    updateNavigation();
});

function getAuthToken() {
    return localStorage.getItem('access_token');
}

function getUserRole() {
    return localStorage.getItem('user_role');
}

function isLoggedIn() {
    return !!getAuthToken();
}

function updateNavigation() {
    const navLinks = document.getElementById('nav-links');
    if (!navLinks) return;

    if (isLoggedIn()) {
        const role = getUserRole();
        let dashboardLink = '/dashboard';
        
        // Construct links based on role
        let html = `
            <a href="/">Home</a>
            <a href="/courses">Courses</a>
            <a href="${dashboardLink}">Dashboard</a>
            <a href="#" onclick="logout(); return false;" style="color: var(--danger)">Logout</a>
        `;
        navLinks.innerHTML = html;
    } else {
        navLinks.innerHTML = `
            <a href="/">Home</a>
            <a href="/courses">Courses</a>
            <a href="/login" class="btn-login">Log In</a>
        `;
    }
}

async function logout() {
    const refresh = localStorage.getItem('refresh_token');
    const access = localStorage.getItem('access_token');
    
    if (refresh && access) {
        try {
            await fetch('/api/auth/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${access}`
                },
                body: JSON.stringify({ refresh })
            });
        } catch (e) {
            console.error('Logout failed on server', e);
        }
    }
    
    // Clear local storage regardless
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_role');
    
    window.location.href = '/login';
}

// Fetch helper with attached auth header
async function apiFetch(url, options = {}) {
    const token = getAuthToken();
    if (!options.headers) options.headers = {};
    if (token) {
        options.headers['Authorization'] = `Bearer ${token}`;
    }
    
    const response = await fetch(url, options);
    
    // Handle 401 Unauthorized (todo: implement token refresh logic)
    if (response.status === 401) {
        logout();
        throw new Error('Unauthorized');
    }
    
    return response;
}
