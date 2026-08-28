// Data opsi unit untuk dropdown sesuai dictionary ConvertNumber FastAPI
const units = {
  length: [
    { label: "Kilometer (km)", value: "km" },
    { label: "Hektometer (hm)", value: "hm" },
    { label: "Dekameter (dam)", value: "dam" },
    { label: "Meter (m)", value: "m" },
    { label: "Desimeter (dm)", value: "dm" },
    { label: "Sentimeter (cm)", value: "cm" },
    { label: "Milimeter (mm)", value: "mm" }
  ],
  weight: [
    { label: "Kilogram (kg)", value: "kg" },
    { label: "Hektogram (hg)", value: "hg" },
    { label: "Dekagram (dag)", value: "dag" },
    { label: "Gram (g)", value: "g" },
    { label: "Desigram (dg)", value: "dg" },
    { label: "Sentigram (cg)", value: "cg" },
    { label: "Miligram (mg)", value: "mg" }
  ],
  tempr: [
    { label: "Celsius (°C)", value: "c" },
    { label: "Reaumur (°R)", value: "r" },
    { label: "Fahrenheit (°F)", value: "f" },
    { label: "Kelvin (K)", value: "k" }
  ]
};

let currentCategory = "length";

// Inisialisasi dropdown saat halaman selesai dimuat
document.addEventListener("DOMContentLoaded", () => {
  populateDropdowns("length");
});

// Mengubah kategori (Length, Weight, Temperature)
function changeCategory(category, evt) {
  currentCategory = category;
  
  // Ubah tampilan tab aktif
  const tabs = document.querySelectorAll('.tab-item');
  tabs.forEach(tab => tab.classList.remove('active'));
  
  if (evt && evt.target) {
    evt.target.classList.add('active');
  }

  // Isi ulang opsi dropdown sesuai kategori
  populateDropdowns(category);
}

// Mengisi opsi ke elemen <select>
function populateDropdowns(category) {
  const selectFrom = document.getElementById("unit-from");
  const selectTo = document.getElementById("unit-to");

  selectFrom.innerHTML = "";
  selectTo.innerHTML = "";

  units[category].forEach((unit) => {
    const opt1 = new Option(unit.label, unit.value);
    const opt2 = new Option(unit.label, unit.value);
    selectFrom.add(opt1);
    selectTo.add(opt2);
  });

  // Pilih unit kedua sebagai default untuk unit tujuan
  if (selectTo.options.length > 1) {
    selectTo.selectedIndex = 1;
  }
}

// Memanggil FastAPI POST /convert
async function handleConvert() {
  const valInput = parseFloat(document.getElementById("val-input").value);
  const unitFrom = document.getElementById("unit-from").value;
  const unitTo = document.getElementById("unit-to").value;

  if (isNaN(valInput)) {
    alert("Masukkan angka yang valid!");
    return;
  }

  // Request Body untuk Pydantic Schema di FastAPI
  const payload = {
    type_unit: currentCategory,
    from_num: valInput,
    unit_from: unitFrom,
    unit_to: unitTo
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/convert", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Gagal melakukan konversi dari server");
    }

    const data = await response.json();

    // Tampilkan hasil konversi
    document.getElementById("result-text").innerText = 
      `${valInput} ${unitFrom.toUpperCase()} = ${data.result_convert} ${unitTo.toUpperCase()}`;
    
    // Toggle visibilitas menggunakan CSS class
    document.getElementById("form-section").classList.add("hidden");
    document.getElementById("result-section").classList.remove("hidden");

  } catch (error) {
    console.error("Fetch Error:", error);
    alert("Error: " + error.message + "\n\nPastikan server FastAPI Anda sudah berjalan di http://127.0.0.1:8000 dan CORS Middleware sudah diaktifkan.");
  }
}

// Mengembalikan ke tampilan form
function handleReset() {
  document.getElementById("form-section").classList.remove("hidden");
  document.getElementById("result-section").classList.add("hidden");
}