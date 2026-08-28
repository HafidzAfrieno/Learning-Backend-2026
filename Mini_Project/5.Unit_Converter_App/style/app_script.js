// Data Satuan Sesuai Instruksi
const unitsData = {
  panjang: {
    label: "Enter the length to convert",
    options: ["milimeter", "sentimeter", "meter", "kilometer", "inci", "kaki", "yard", "mil"]
  },
  berat: {
    label: "Enter the weight to convert",
    options: ["miligram", "gram", "kilogram", "ons", "pon"]
  },
  suhu: {
    label: "Enter the temperature to convert",
    options: ["Celcius", "Fahrenheit", "Kelvin"]
  }
};

let currentCategory = 'panjang';

function populateSelects(category) {
  const fromSelect = document.getElementById('unit-from');
  const toSelect = document.getElementById('unit-to');
  const inputLabel = document.getElementById('input-label');

  inputLabel.innerText = unitsData[category].label;
  fromSelect.innerHTML = '';
  toSelect.innerHTML = '';

  unitsData[category].options.forEach((unit) => {
    fromSelect.add(new Option(unit, unit));
    toSelect.add(new Option(unit, unit));
  });

  // Atur nilai default dropdown kedua agar beda dari yang pertama
  if (toSelect.options.length > 1) {
    toSelect.selectedIndex = 1;
  }
}

function changeCategory(category) {
  currentCategory = category;
  
  // Update UI Tab Active
  const tabs = document.querySelectorAll('.tab-item');
  tabs.forEach(tab => tab.classList.remove('active'));
  
  const categoryIndex = category === 'panjang' ? 0 : category === 'berat' ? 1 : 2;
  tabs[categoryIndex].classList.add('active');

  populateSelects(category);
  handleReset();
}

async function handleConvert() {
  const value = document.getElementById('val-input').value;
  const fromUnit = document.getElementById('unit-from').value;
  const toUnit = document.getElementById('unit-to').value;

  if (!value && value !== 0) {
    alert("Silakan masukkan nilai terlebih dahulu.");
    return;
  }

  // ===========================================================
  // BAGIAN INTEGRASI API PYTHON (Mengarahkan ke port lokal 8000)
  // ===========================================================
  try {
    const response = await fetch('http://127.0.0.1:8000/api/convert', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        category: currentCategory,
        value: parseFloat(value),
        from: fromUnit,
        to: toUnit
      })
    });

    if (!response.ok) {
      alert("Gagal melakukan konversi dari API.");
      return;
    }

    const data = await response.json();
    
    // Menampilkan hasil konversi asli dari FastAPI
    displayResult(`${value} ${fromUnit} = ${data.result} ${toUnit}`);
  } catch (error) {
    console.error("Error connecting to API:", error);
    alert("Gagal terhubung ke server FastAPI. Pastikan Uvicorn di port 8000 sudah berjalan.");
  }
}

function displayResult(textResult) {
  document.getElementById('result-text').innerText = textResult;
  document.getElementById('form-section').classList.add('hidden');
  document.getElementById('result-section').classList.remove('hidden');
}

function handleReset() {
  document.getElementById('form-section').classList.remove('hidden');
  document.getElementById('result-section').classList.add('hidden');
}

// Inisialisasi awal
populateSelects('panjang');