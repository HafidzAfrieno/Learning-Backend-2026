const units = {
      panjang: ["Milimeter", "Sentimeter", "Meter", "Kilometer", "Inci", "Kaki", "Yard", "Mil"],
      berat: ["Miligram", "Gram", "Kilogram", "Ons", "Pon"],
      suhu: ["Celcius", "Fahrenheit", "Kelvin"]
    };

    let currentCategory = 'panjang';

    function renderOptions(category) {
      const fromSelect = document.getElementById('unit-from');
      const toSelect = document.getElementById('unit-to');
      
      fromSelect.innerHTML = '';
      toSelect.innerHTML = '';

      units[category].forEach((unit, index) => {
        const option1 = new Option(unit, unit.toLowerCase());
        const option2 = new Option(unit, unit.toLowerCase());
        fromSelect.add(option1);
        toSelect.add(option2);
      });

      // Default pilih opsi kedua untuk dropdown "Ke" agar berbeda
      if (toSelect.options.length > 1) {
        toSelect.selectedIndex = 1;
      }
    }

    function switchTab(category) {
      currentCategory = category;
      
      // Update UI Tab Active
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.innerText.toLowerCase() === category) {
          btn.classList.add('active');
        }
      });

      renderOptions(category);
    }

    // Inisialisasi awal
    renderOptions(currentCategory);