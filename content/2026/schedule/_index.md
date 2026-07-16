---
title: Schedule
year: 2026
type: schedule
draft: false
horizontal: false
suggestion: "Please note that minor adjustments may occur as we approach the event date."
menu:
    2026:
        weight: 2
        identifier: schedule
        parent: attend
---


<style>
/* QCrypt 2026 card-based schedule with sticky day selector */
html { scroll-behavior: smooth; }

.qc-schedule {
  max-width: 1180px;
  margin: 0 auto;
  padding: 1rem 0 3rem;
}

.qc-intro {
  margin: 0 0 1.5rem;
  font-size: 1.08rem;
  color: #4a4a4a;
}

.qc-day-nav {
  position: sticky;
  top: 80px;
  z-index: 1000;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  background: rgba(255, 255, 255, .96);
  backdrop-filter: blur(4px);
  padding: 14px 15px;
  margin: 25px 0 40px;
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  box-shadow: 0 3px 12px rgba(0,0,0,.10);
}

.qc-day-nav button {
  border: none;
  appearance: none;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 999px;
  background: #eef4fb;
  color: #003366;
  font-weight: 700;
  cursor: pointer;
  transition: all .2s ease;
}

.qc-day-nav button:hover,
.qc-day-nav button:focus {
  background: #d7e8fa;
  transform: translateY(-1px);
}

.qc-day-nav button.active {
  background: #003366;
  color: #ffffff;
}

.qc-day {
  display: none;
  margin-top: 3.25rem;
  scroll-margin-top: 150px;
}

.qc-day.is-active {
  display: block;
}

.qc-day-title {
  font-size: clamp(2rem, 4vw, 3.15rem);
  font-weight: 300;
  line-height: 1.1;
  color: #3f3f3f;
  margin: 0 0 1.5rem;
  padding-bottom: .65rem;
  border-bottom: 2px solid #003366;
}

.qc-row {
  display: flex;
  align-items: stretch;
  gap: 1.15rem;
  margin-bottom: 1rem;
}

.qc-time {
  width: 130px;
  flex: 0 0 130px;
  color: #515151;
  text-align: right;
  padding-top: .68rem;
  line-height: .95;
}

.qc-time .hour {
  display: inline-block;
  font-size: clamp(2rem, 4vw, 3.1rem);
  font-weight: 300;
  letter-spacing: -1px;
}

.qc-time .minute {
  display: inline-block;
  font-size: 1.22rem;
  font-weight: 300;
  vertical-align: .7em;
  margin-left: .12rem;
}

.qc-time .range {
  display: block;
  margin-top: .38rem;
  font-size: .8rem;
  color: #777;
  letter-spacing: .02em;
}

.qc-card {
  flex: 1 1 auto;
  min-width: 0;
  background: #ffffff;
  border: 1px solid #dddddd;
  border-left: 7px solid #3d7ea6;
  border-radius: 10px;
  box-shadow: 0 2px 7px rgba(0, 0, 0, .11);
  padding: .85rem 1rem .95rem;
}

.qc-card-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: flex-start;
  border-bottom: 1px solid rgba(0,0,0,.06);
  padding-bottom: .5rem;
  margin-bottom: .55rem;
}

.qc-title {
  margin: 0;
  font-size: 1.1rem;
  line-height: 1.35;
  font-weight: 600;
  color: #2d2d2d;
}

.qc-badge {
  flex: 0 0 auto;
  display: inline-block;
  padding: .22rem .58rem;
  border-radius: 999px;
  font-size: .72rem;
  text-transform: uppercase;
  letter-spacing: .04em;
  font-weight: 800;
  background: #eef2f6;
  color: #4b5563;
  white-space: nowrap;
}

.qc-speaker {
  font-weight: 800;
  font-size: 1rem;
  color: #24384a;
  margin-top: .35rem;
}

.qc-affiliation,
.qc-location {
  color: #666;
  font-size: .92rem;
  margin-top: .16rem;
}

.qc-location::before {
  content: "Location: ";
  font-weight: 700;
  color: #555;
}

.qc-card.break { background: #eaf4ff; border-left-color: #7aa7d9; }
.qc-card.social { background: #fff6df; border-left-color: #d9a441; }
.qc-card.tutorial { background: #f8fbff; border-left-color: #2f75b5; }
.qc-card.invited { background: #ffffff; border-left-color: #5c8f42; }
.qc-card.contributed { background: #fafafa; border-left-color: #6c757d; }
.qc-card.program { background: #eef8ee; border-left-color: #5f9b5f; }

.qc-note {
  margin-top: 2.5rem;
  padding: 1rem 1.25rem;
  background: #f7f7f7;
  border-left: 5px solid #777;
  color: #444;
}

@media (max-width: 768px) {
  .qc-day-nav { top: 0; }
  .qc-row { flex-direction: column; gap: .35rem; }
  .qc-time {
    width: auto;
    flex-basis: auto;
    text-align: left;
    padding-top: 0;
  }
  .qc-time .hour { font-size: 2rem; }
  .qc-card-header { flex-direction: column; gap: .45rem; }
}
</style>

<div class="qc-schedule">

# Program

<!-- <p class="qc-intro"><strong>University of Ottawa</strong><br>August 24–28, 2026</p> -->

<nav class="qc-day-nav" aria-label="Schedule days">
  <button type="button" data-day="monday" onclick="showDay('monday')" class="active">Monday, August 24</button>
  <button type="button" data-day="tuesday" onclick="showDay('tuesday')">Tuesday, August 25</button>
  <button type="button" data-day="wednesday" onclick="showDay('wednesday')">Wednesday, August 26</button>
  <button type="button" data-day="thursday" onclick="showDay('thursday')">Thursday, August 27</button>
  <button type="button" data-day="friday" onclick="showDay('friday')">Friday, August 28</button>
</nav>

<section class="qc-day is-active" id="monday">
<h2 class="qc-day-title">Monday, August 24, 2026</h2>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">15</span>
    <span class="range">08:15–09:00</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Conference Check-in &amp; Light Breakfast</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C100K; C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">00</span>
    <span class="range">09:00–09:15</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Welcoming Speech</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">15</span>
    <span class="range">09:15–10:30</span>
  </div>
  <article class="qc-card tutorial">
    <div class="qc-card-header">
      <h3 class="qc-title">Tutorial Talk: Self-testing in quantum cryptography</h3>
      <span class="qc-badge">Tutorial</span>
    </div>
    <div class="qc-speaker">Ivan Šupi</div>
    <div class="qc-affiliation">LIG - CNRS/Université Grenoble Alpes</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">30</span>
    <span class="range">10:30–11:00</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">00</span>
    <span class="range">11:00–11:45</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Quantum statistics in the minimal Bell scenario</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Jean-Daniel Bancal</div>
    <div class="qc-affiliation">Institut de Physique Théorique Saclay</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">45</span>
    <span class="range">11:45–12:30</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Less is More: On Copy Complexity in Quantum Cryptography</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Eli Goldin</div>
    <div class="qc-affiliation">New York University</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">30</span>
    <span class="range">12:30–14:00</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Lunch at CRX</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">Dining Hall (UCU 85 Univ.) G01</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">00</span>
    <span class="range">14:00–14:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #63 Compressed Permutation Oracles</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">20</span>
    <span class="range">14:20–14:40</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #22 The Sponge is Quantum Indifferentiable</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">40</span>
    <span class="range">14:40–15:00</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #74 Post-quantum security of block cipher constructions</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">00</span>
    <span class="range">15:00–15:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #18 Quantum Oracle Distribution Switching and its Applications to Fully Anonymous Ring Signatures</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">20</span>
    <span class="range">15:20–15:50</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">50</span>
    <span class="range">15:50–16:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #33 Rethinking quantum smooth entropies: Tight one-shot analysis of quantum privacy amplification</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">10</span>
    <span class="range">16:10–16:30</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #7 A rigorous and complete security proof of decoy-state BB84 quantum key distribution</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">30</span>
    <span class="range">16:30–16:50</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #95 Rigorous phase-error-estimation security framework for QKD with correlated sources</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">50</span>
    <span class="range">16:50–17:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #128 Simplified quantum key distribution implementation secure against state preparation flaws</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">10</span>
    <span class="range">17:10–17:30</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #43 Unconditional Authentication in Quantum Key Distribution via Hybrid Entangled Physical Unclonable Functions</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">30</span>
    <span class="range">17:30–17:50</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #24 QKD Oracles for Authenticated Key Exchange</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">50</span>
    <span class="range">17:50–19:20</span>
  </div>
  <article class="qc-card social">
    <div class="qc-card-header">
      <h3 class="qc-title">Poster Session and Reception (Even Numbers)</h3>
      <span class="qc-badge">Social</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

</section>

<section class="qc-day" id="tuesday">
<h2 class="qc-day-title">Tuesday, August 25, 2026</h2>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">15</span>
    <span class="range">08:15–08:55</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Light Breakfast</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">55</span>
    <span class="range">08:55–09:00</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Updates &amp; Announcements</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240; C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">00</span>
    <span class="range">09:00–10:15</span>
  </div>
  <article class="qc-card tutorial">
    <div class="qc-card-header">
      <h3 class="qc-title">Tutorial Talk: Continuous-Variable Quantum Key Distribution</h3>
      <span class="qc-badge">Tutorial</span>
    </div>
    <div class="qc-speaker">Tobias Gehring</div>
    <div class="qc-affiliation">Technical University of Denmark</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">15</span>
    <span class="range">10:15–10:45</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">45</span>
    <span class="range">10:45–11:30</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Quantum communication takes to the skies</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Paul G. Kwiat</div>
    <div class="qc-affiliation">University of Illinois at Urbana-Champaign</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">30</span>
    <span class="range">11:30–12:15</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Quantum communication with ultrafast time-Bin encoding</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Duncan England</div>
    <div class="qc-affiliation">National Research Council of Canada</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">15</span>
    <span class="range">12:15–12:30</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Group Photo</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">Location to be communicated soon</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">30</span>
    <span class="range">12:30–14:00</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Lunch at CRX</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">Dining Hall (UCU 85 Univ.) G01</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">00</span>
    <span class="range">14:00–14:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #8/#100 Uncloneable encryption from decoupling / The uncloneable bit exists</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">20</span>
    <span class="range">14:20–14:40</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #62 Multi-Copy Security in Quantum Cryptography and More</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">40</span>
    <span class="range">14:40–15:00</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #52 Towards Universal Quantum Tamper Detection</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">00</span>
    <span class="range">15:00–15:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #139 Proofs of Quantum Memory</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">20</span>
    <span class="range">15:20–15:50</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">50</span>
    <span class="range">15:50–16:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #14 Hierarchical generation and design of tree-codes for resource-efficient loss-tolerant quantum communications</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">10</span>
    <span class="range">16:10–16:30</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #19 Quantification of the energy consumption of entanglement distribution</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">30</span>
    <span class="range">16:30–16:50</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #65 Chip-based Long-distance Twin-field Quantum Key Distribution Networks</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">16</span><span class="minute">50</span>
    <span class="range">16:50–17:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #104 Long-Distance Free-Space Twin-Field Quantum Key Distribution towards Satellite-based Quantum Network</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">10</span>
    <span class="range">17:10–17:30</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #89 Reference-beam attacks against OIL-based Twin-Field QKD</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">30</span>
    <span class="range">17:30–17:50</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #69 Continuous-variable quantum communication over hybrid channels</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">50</span>
    <span class="range">17:50–18:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #101 High-Performance Laser Written Heterodyne Receiver for Photonic Quantum Information Processing</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">18</span><span class="minute">10</span>
    <span class="range">18:10–19:40</span>
  </div>
  <article class="qc-card social">
    <div class="qc-card-header">
      <h3 class="qc-title">Poster Session and Reception (Odd Numbers)</h3>
      <span class="qc-badge">Social</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

</section>

<section class="qc-day" id="wednesday">
<h2 class="qc-day-title">Wednesday, August 26, 2026</h2>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">15</span>
    <span class="range">08:15–08:55</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Light Breakfast</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">55</span>
    <span class="range">08:55–09:00</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Updates &amp; Announcements</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240; C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">00</span>
    <span class="range">09:00–10:15</span>
  </div>
  <article class="qc-card tutorial">
    <div class="qc-card-header">
      <h3 class="qc-title">Tutorial Talk: Quantum cryptography beyond QKD: advances and practical challenges</h3>
      <span class="qc-badge">Tutorial</span>
    </div>
    <div class="qc-speaker">Mathieu Bozzio</div>
    <div class="qc-affiliation">University of Vienna</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">15</span>
    <span class="range">10:15–10:45</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">45</span>
    <span class="range">10:45–11:30</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Relativistic Position Verification with Coherent States</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Guan-Jie Fan-Yuan</div>
    <div class="qc-affiliation">University of Science and Technology of China</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">30</span>
    <span class="range">11:30–12:15</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Free-Space Twin-Field Quantum Key Distribution</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Yu-Huai Li</div>
    <div class="qc-affiliation">University of Science and Technology of China</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">15</span>
    <span class="range">12:15–13:00</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Lunch Boxes</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">Dining Hall (UCU 85 Univ.) G01</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">13</span><span class="minute">00</span>
    <span class="range">13:00–19:00</span>
  </div>
  <article class="qc-card social">
    <div class="qc-card-header">
      <h3 class="qc-title">Nexus for Quantum Technologies (NexQT) Laboratory Tour, Electric Boat Cruise &amp; Downtown Ottawa &amp; Outdoor Adventure at Camp Fortune</h3>
      <span class="qc-badge">Social</span>
    </div>
    <div class="qc-location">Locations to be communicated soon</div>
  </article>
</div>

</section>

<section class="qc-day" id="thursday">
<h2 class="qc-day-title">Thursday, August 27, 2026</h2>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">15</span>
    <span class="range">08:15–08:55</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Light Breakfast</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">55</span>
    <span class="range">08:55–09:00</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Updates &amp; Announcements</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240; C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">00</span>
    <span class="range">09:00–10:15</span>
  </div>
  <article class="qc-card tutorial">
    <div class="qc-card-header">
      <h3 class="qc-title">Tutorial Talk: Security Proofs for Quantum Key Distribution</h3>
      <span class="qc-badge">Tutorial</span>
    </div>
    <div class="qc-speaker">Ramona Wolf</div>
    <div class="qc-affiliation">University of Innsbruck</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">15</span>
    <span class="range">10:15–10:45</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">45</span>
    <span class="range">10:45–11:30</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: Private Proofs of When and Where</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Tal Malkin</div>
    <div class="qc-affiliation">Columbia University</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">30</span>
    <span class="range">11:30–12:15</span>
  </div>
  <article class="qc-card invited">
    <div class="qc-card-header">
      <h3 class="qc-title">Invited Talk: On obfuscating quantum computation</h3>
      <span class="qc-badge">Invited</span>
    </div>
    <div class="qc-speaker">Mi-Ying Miryam Huang</div>
    <div class="qc-affiliation">University of Southern California</div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">15</span>
    <span class="range">12:15–13:45</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Lunch at CRX</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">Dining Hall (UCU 85 Univ.) G01</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">13</span><span class="minute">45</span>
    <span class="range">13:45–14:05</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #21 Quantitative quantum soundness for all multipartite compiled nonlocal games</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">05</span>
    <span class="range">14:05–14:25</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #108 Reliable Entropy Estimation for device-independent QKD based on Layer-Cake Representations of Divergences</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">25</span>
    <span class="range">14:25–14:45</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #109 QKD with local self-testing: device-independent security and device-dependent performance</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">14</span><span class="minute">45</span>
    <span class="range">14:45–15:05</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #131 Robust One-Sided Device-Independent Quantum Key Distribution via High-Dimensional Steering</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">05</span>
    <span class="range">15:05–15:35</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">15</span><span class="minute">35</span>
    <span class="range">15:35–17:15</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Industry Panel: Quantum Satellite Infrastructure and Applications</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">17</span><span class="minute">15</span>
    <span class="range">17:15–17:45</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Business Meeting</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">18</span><span class="minute">30</span>
    <span class="range">18:30–21:30</span>
  </div>
  <article class="qc-card social">
    <div class="qc-card-header">
      <h3 class="qc-title">Gala Dinner, Awards and Networking at National Arts Centre</h3>
      <span class="qc-badge">Social</span>
    </div>
    <div class="qc-location">National Arts Centre</div>
  </article>
</div>

</section>

<section class="qc-day" id="friday">
<h2 class="qc-day-title">Friday, August 28, 2026</h2>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">15</span>
    <span class="range">08:15–08:55</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Light Breakfast</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">08</span><span class="minute">55</span>
    <span class="range">08:55–09:00</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Updates &amp; Announcements</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240; C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">00</span>
    <span class="range">09:00–09:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #15 On Removing Interaction from Quantum Proofs</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">20</span>
    <span class="range">09:20–09:40</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #44 Security of the Fischlin Transform in the Quantum Random Oracle Model</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">09</span><span class="minute">40</span>
    <span class="range">09:40–10:00</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #48 Composable Verification in the Circuit-Model via Magic-Blindness</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">00</span>
    <span class="range">10:00–10:20</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #61 How to Delete Without a Trace: Certified Deniability in a Quantum World</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">10</span><span class="minute">20</span>
    <span class="range">10:20–11:20</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Hot Topics Meeting</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">20</span>
    <span class="range">11:20–11:50</span>
  </div>
  <article class="qc-card break">
    <div class="qc-card-header">
      <h3 class="qc-title">Coffee Break</h3>
      <span class="qc-badge">Break</span>
    </div>
    <div class="qc-location">C130, C100A, C100H</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">11</span><span class="minute">50</span>
    <span class="range">11:50–12:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #3 Comparing classical and quantum conditional disclosure of secrets</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">10</span>
    <span class="range">12:10–12:30</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #78 Hybrid Quantum Cryptography from Communication Complexity: From Theory to Experimental benchmarking</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">30</span>
    <span class="range">12:30–12:50</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #64 Non Interactive MPC, (Quantumly) Revisited</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">12</span><span class="minute">50</span>
    <span class="range">12:50–13:10</span>
  </div>
  <article class="qc-card contributed">
    <div class="qc-card-header">
      <h3 class="qc-title">Contributed Talk: #113 Quantum-Secure Private Inference from Vacuum Fluctuations</h3>
      <span class="qc-badge">Contributed</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

<div class="qc-row">
  <div class="qc-time">
    <span class="hour">13</span><span class="minute">10</span>
    <span class="range">13:10–13:30</span>
  </div>
  <article class="qc-card program">
    <div class="qc-card-header">
      <h3 class="qc-title">Closing Remarks</h3>
      <span class="qc-badge">Program</span>
    </div>
    <div class="qc-location">C140, C240</div>
  </article>
</div>

</section>

<div class="qc-note"><strong>Note:</strong> The program may be subject to minor changes. Please check this page for updates.</div>
</div>

<script>
function showDay(dayId) {
  document.querySelectorAll('.qc-day').forEach(function(day) {
    day.classList.remove('is-active');
  });

  var selectedDay = document.getElementById(dayId);
  if (selectedDay) {
    selectedDay.classList.add('is-active');
  }

  document.querySelectorAll('.qc-day-nav button').forEach(function(button) {
    button.classList.remove('active');
  });

  var selectedButton = document.querySelector('.qc-day-nav button[data-day="' + dayId + '"]');
  if (selectedButton) {
    selectedButton.classList.add('active');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  showDay('monday');
});
</script>

<!--<div class="qc-note"><strong>Note:</strong> The program is subject to change. Please check this page for updates.</div>
</div>

Please note that minor adjustments may occur as we approach the event date_ 

<center>

<iframe src="https://calendar.google.com/calendar/embed?src=907f21784a2ffb01aeba27bd482e9f6ffe74724ad532cff170c473254a237179%40group.calendar.google.com&ctz=America%2FToronto" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

<iframe src="https://calendar.google.com/calendar/embed?src=907f21784a2ffb01aeba27bd482e9f6ffe74724ad532cff170c473254a237179%40group.calendar.google.com&ctz=America%2FToronto" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe> 

<iframe src="https://calendar.google.com/calendar/embed?height=800&amp;wkst=2&amp;bgcolor=%23ffffff&amp;ctz=Europe%2FAmsterdam&amp;src=NGY5cnZsdW5tbXJrcGloMWlibzExZ29vNjRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%23E4C441&amp;color=%234285F4&amp;mode=AGENDA" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe> 

</center>  -->
