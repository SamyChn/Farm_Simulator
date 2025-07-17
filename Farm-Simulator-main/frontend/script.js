const API_URL = 'http://127.0.0.1:5000';

async function fetchFields() {
    const stateFilter = document.getElementById("stateFilter").value;
    let url = `${API_URL}/fields`;

    if (stateFilter !== "all") {
        url += `?state=${encodeURIComponent(stateFilter)}`;
    }

    const response = await fetch(url);
    const fields = await response.json();
    const tbody = document.querySelector('#fieldsTable tbody');
    tbody.innerHTML = '';
    fields.forEach(field => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${field.id}</td>
            <td>${field.name}</td>
            <td>${field.crop_type}</td>
            <td>${field.state}</td>
            <td>${new Date(field.last_action).toLocaleString()}</td>
            <td>
                <button onclick="plant(${field.id})">🌱 Semer</button>
                <button onclick="harvest(${field.id})">🚜 Récolter</button>
                <button onclick="reset(${field.id})">❌ Vider</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

async function plant(id) {
    const crop = prompt("Quelle culture voulez-vous semer ? (ex: blé, maïs)");
    if (crop) {
        await fetch(`${API_URL}/fields/${id}/plant?crop=${encodeURIComponent(crop)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ crop })
        });
        fetchFields();
    }
}

async function harvest(id) {
    await fetch(`${API_URL}/fields/${id}/harvest`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    fetchFields();
}

async function reset(id) {
    await fetch(`${API_URL}/fields/${id}/reset`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    fetchFields();
}


fetchFields();
