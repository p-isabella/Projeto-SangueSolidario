const calendarDates = document.querySelector('.calendar-dates');
const monthYear = document.getElementById('month-year');
const prevMonthBtn = document.getElementById('prev-month');
const nextMonthBtn = document.getElementById('next-month');
const confirmBtn = document.getElementById('confirm-btn');
const selectedDateDisplay = document.getElementById('selected-date-display');
const timeSlotPanel = document.getElementById('time-slot-panel');
const timeSlotGrid = document.getElementById('time-slot-grid');
const timeSlotTitle = document.getElementById('time-slot-title');
const selectedTimeDisplay = document.getElementById('selected-time-display');

let currentDate = new Date();
let currentMonth = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

const months = [
  'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];

const TIME_SLOTS = [
  '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
  '10:00', '10:30', '11:00', '11:30', '13:00', '13:30',
  '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'
];

let savedDates = JSON.parse(localStorage.getItem('selectedDates') || '[]');
let selectedTime = localStorage.getItem('selectedTime') || null;

const today = new Date();
today.setHours(0, 0, 0, 0);

function renderTimeSlots(dateKey) {
  timeSlotGrid.innerHTML = '';

  TIME_SLOTS.forEach(time => {
    const slot = document.createElement('div');
    slot.classList.add('time-slot');
    slot.textContent = time;

    if (selectedTime === time) {
      slot.classList.add('selected-time');
      updateTimeConfirm(time, dateKey);
    }

    slot.addEventListener('click', () => {
      document.querySelectorAll('.time-slot.selected-time')
        .forEach(el => el.classList.remove('selected-time'));

      slot.classList.add('selected-time');
      selectedTime = time;
      localStorage.setItem('selectedTime', time);

      sessionStorage.setItem(
        'agendamento',
        JSON.stringify({ data: dateKey, hora: time })
      );

      updateTimeConfirm(time, dateKey);
    });

    timeSlotGrid.appendChild(slot);
  });
}

function updateTimeConfirm(time, dateKey) {
  const [year, month, day] = dateKey.split('-');
  selectedTimeDisplay.textContent = `Agendamento: ${day}/${month}/${year} às ${time}`;
  confirmBtn.disabled = false;
}

function openTimePanel(dateLabel, dateKey) {
  timeSlotTitle.textContent = `Horários disponíveis — ${dateLabel}`;
  renderTimeSlots(dateKey);
  timeSlotPanel.classList.add('open');
  setTimeout(() => {
    timeSlotPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }, 50);
}

function renderCalendar(month, year) {
  calendarDates.innerHTML = '';
  monthYear.textContent = `${months[month]} ${year}`;

  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  for (let i = 0; i < firstDay; i++) {
    const blank = document.createElement('div');
    calendarDates.appendChild(blank);
  }

  for (let i = 1; i <= daysInMonth; i++) {
    const day = document.createElement('div');
    day.textContent = i;

    const dateKey = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`;
    const thisDate = new Date(year, month, i);

    if (savedDates.includes(dateKey)) {
      day.classList.add('selected');
    }

    if (thisDate < today) {
      day.classList.add('disabled');
    } else {
      day.addEventListener('click', () => {
        document.querySelectorAll('.calendar-dates div.selected')
          .forEach(el => el.classList.remove('selected'));

        savedDates = [dateKey];
        day.classList.add('selected');

        const dayLabel = `${String(i).padStart(2,'0')}/${String(month+1).padStart(2,'0')}/${year}`;
        selectedDateDisplay.textContent = `Data selecionada: ${dayLabel}`;

        selectedTime = null;
        localStorage.removeItem('selectedTime');
        confirmBtn.disabled = true;
        selectedTimeDisplay.textContent = 'Selecione um horário.';

        localStorage.setItem('selectedDates', JSON.stringify(savedDates));

        openTimePanel(dayLabel, dateKey);
      });
    }

    calendarDates.appendChild(day);
  }
}

renderCalendar(currentMonth, currentYear);

if (savedDates.length > 0) {
  const [yr, mo, dy] = savedDates[0].split('-');
  const dayLabel = `${dy}/${mo}/${yr}`;
  selectedDateDisplay.textContent = `Data selecionada: ${dayLabel}`;
  openTimePanel(dayLabel, savedDates[0]);
}

prevMonthBtn.addEventListener('click', () => {
  currentMonth--;
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  renderCalendar(currentMonth, currentYear);
});

nextMonthBtn.addEventListener('click', () => {
  currentMonth++;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  renderCalendar(currentMonth, currentYear);
});

// requisicao
confirmBtn.addEventListener('click', () => {
  if (confirmBtn.disabled) return;
  window.location.href = '/usuario/agendamento/informacoes';
});