import os

import pandas as pd
import streamlit as st


st.set_page_config(
	page_title="Cyrus Bayquen | Aspiring Programmer",
	page_icon="CB",
	layout="wide",
	initial_sidebar_state="collapsed",
)

st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');

	:root {
		--paper: #f5f1e9;
		--ink: #18202a;
		--muted: #66707c;
		--blue: #1459e6;
		--yellow: #f3ca42;
		--line: #d8d2c7;
		--white: #fffdf8;
	}
	.stApp { background: var(--paper); color: var(--ink); }
	[data-testid="stHeader"] { background: rgba(245, 241, 233, 0.86); }
	.block-container { max-width: 1160px; padding: 2rem 3rem 4rem; }
	.mono, code, .eyebrow { font-family: 'DM Mono', monospace; }
	.eyebrow { color: var(--blue); font-size: .74rem; letter-spacing: .09em; text-transform: uppercase; }
	.topbar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--line); padding-bottom: 1.2rem; margin-bottom: 3.6rem; }
	.brand { font: 700 1.15rem 'Space Grotesk', sans-serif; letter-spacing: -.04em; }
	.brand span { color: var(--blue); }
	.availability { color: var(--muted); font: .74rem 'DM Mono', monospace; }
	.availability b { color: #31915d; font-size: 1.2rem; vertical-align: -1px; }
	.hero-copy { padding: 1rem 0 0; }
	h1 { color: var(--ink); font: 700 clamp(3.5rem, 8vw, 7.5rem)/.86 'Space Grotesk', sans-serif; letter-spacing: -.09em; margin: .75rem 0 1.8rem; }
	.hero-copy p { color: var(--muted); font: 1.05rem/1.6 'Space Grotesk', sans-serif; max-width: 470px; }
	.hero-copy strong { color: var(--ink); }
	.terminal { background: #18202a; color: #e7edf5; border: 1px solid #18202a; box-shadow: 12px 12px 0 var(--yellow); margin: .5rem .8rem 1rem 0; }
	.terminal-head { background: #27313e; color: #9ca8b5; font: .7rem 'DM Mono', monospace; padding: .7rem 1rem; }
	.dots { color: #f3ca42; letter-spacing: .2em; }
	.terminal-body { padding: 1.5rem 1.6rem 1.7rem; font: .83rem/1.85 'DM Mono', monospace; min-height: 245px; }
	.prompt { color: #62d49a; }
	.command { color: #f3ca42; }
	.code-blue { color: #6fb0ff; }
	.terminal-note { color: #99a6b5; }
	.section { border-top: 1px solid var(--line); padding-top: 1.4rem; margin-top: 6rem; }
	.section-title { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2rem; }
	h2 { font: 600 2.2rem 'Space Grotesk', sans-serif; letter-spacing: -.06em; margin: 0; }
	.number { color: var(--blue); font: .75rem 'DM Mono', monospace; }
	.project { background: var(--white); border: 1px solid var(--line); padding: 1.5rem; min-height: 260px; transition: transform .2s ease; }
	.project:hover { transform: translateY(-5px); }
	.project-index { color: var(--blue); font: .75rem 'DM Mono', monospace; }
	.project h3 { font: 600 1.45rem 'Space Grotesk', sans-serif; letter-spacing: -.04em; margin: 2.8rem 0 .7rem; }
	.project p { color: var(--muted); line-height: 1.5; margin-bottom: 1.4rem; }
	.tag { color: var(--ink); background: #e9efff; display: inline-block; font: .68rem 'DM Mono', monospace; margin: .18rem .2rem 0 0; padding: .38rem .55rem; }
	.about-copy { color: var(--muted); font: 1.15rem/1.65 'Space Grotesk', sans-serif; max-width: 620px; }
	.about-copy em { color: var(--blue); font-style: normal; }
	.facts { border-left: 2px solid var(--yellow); padding-left: 1.2rem; color: var(--muted); font: .82rem/2 'DM Mono', monospace; }
	.facts b { color: var(--ink); font-weight: 500; }
	.contact { background: var(--blue); color: white; padding: 2.1rem 2.3rem; margin-top: 6rem; display: flex; justify-content: space-between; align-items: center; gap: 2rem; }
	.contact h2 { color: white; }
	.contact p { color: #cbdcff; margin: .5rem 0 0; }
	.contact a { color: var(--ink); background: var(--yellow); font: 500 .8rem 'DM Mono', monospace; padding: .8rem 1rem; text-decoration: none; white-space: nowrap; }
	.footer { color: var(--muted); border-top: 1px solid var(--line); font: .7rem 'DM Mono', monospace; margin-top: 2rem; padding-top: 1.2rem; }
	@media (max-width: 700px) { .block-container { padding: 1.2rem 1.2rem 3rem; } .topbar { margin-bottom: 2.5rem; } .availability { display: none; } .terminal { margin-top: 2.5rem; } .section, .contact { margin-top: 4rem; } .contact { align-items: flex-start; flex-direction: column; } }
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	"""
	<div class="topbar">
		<div class="brand">CYRUS<span>.</span>BAYQUEN</div>
		<div class="availability"><b>•</b>&nbsp; OPEN TO OPPORTUNITIES</div>
	</div>
	<div class="hero-copy">
		<div class="eyebrow">Aspiring programmer / builder</div>
		<h1>Cyrus<br>Bayquen<span style="color:#1459e6">.</span></h1>
		<p>I am learning to turn curious questions into <strong>useful, thoughtful software.</strong> This is a small collection of what I am building, studying, and exploring.</p>
	</div>
	""",
	unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.05, 1], gap="large")
with hero_left:
	st.markdown(
		"""
		<div class="facts" style="margin-top:2rem">
			<div><b>FOCUS</b>&nbsp;&nbsp; Python · web apps · data</div>
			<div><b>BASED</b>&nbsp;&nbsp; Philippines</div>
			<div><b>STATUS</b>&nbsp; Building in public</div>
		</div>
		""",
		unsafe_allow_html=True,
	)
with hero_right:
	st.markdown(
		"""
		<div class="terminal">
			<div class="terminal-head"><span class="dots">● ● ●</span>&nbsp;&nbsp; cyrus@portfolio: ~</div>
			<div class="terminal-body">
				<div><span class="prompt">cyrus@dev</span>:<span class="code-blue">~</span>$ <span class="command">whoami</span></div>
				<div>Cyrus Bayquen</div>
				<br>
				<div><span class="prompt">cyrus@dev</span>:<span class="code-blue">~</span>$ <span class="command">cat interests.txt</span></div>
				<div class="terminal-note">creative tools<br>clean interfaces<br>learning by making</div>
				<br>
				<div><span class="prompt">cyrus@dev</span>:<span class="code-blue">~</span>$ <span class="command">_</span></div>
			</div>
		</div>
		""",
		unsafe_allow_html=True,
	)

st.markdown('<div class="section" id="work"><div class="section-title"><h2>Selected work</h2><span class="number">01 / PROJECTS</span></div></div>', unsafe_allow_html=True)
project_columns = st.columns(3, gap="medium")
projects = [
	("01", "Language tracker", "A first data project for comparing programming languages and measuring progress over time.", ["Python", "Pandas", "Streamlit"]),
	("02", "Weather explorer", "A compact dashboard that turns raw weather records into something easier to read and understand.", ["Python", "Data viz", "CSV"]),
	("03", "Next experiment", "A space reserved for the next idea: small in scope, useful in practice, and shipped with care.", ["Learning", "Building", "Iteration"]),
]
for column, (index, title, description, tags) in zip(project_columns, projects):
	with column:
		tag_markup = "".join(f'<span class="tag">{tag}</span>' for tag in tags)
		st.markdown(f'<div class="project"><div class="project-index">{index} — 2026</div><h3>{title}</h3><p>{description}</p>{tag_markup}</div>', unsafe_allow_html=True)

st.markdown('<div class="section" id="about"><div class="section-title"><h2>A little about me</h2><span class="number">02 / ABOUT</span></div></div>', unsafe_allow_html=True)
about_left, about_right = st.columns([1.3, .7], gap="large")
with about_left:
	st.markdown('<div class="about-copy">I am an aspiring programmer who enjoys the moment an idea becomes something you can click, test, and improve. I am currently deepening my foundations in <em>Python</em>, exploring data, and practicing how to make digital tools feel clear and human.</div>', unsafe_allow_html=True)
with about_right:
	st.markdown('<div class="facts"><div><b>01</b>&nbsp; Stay curious</div><div><b>02</b>&nbsp; Make it useful</div><div><b>03</b>&nbsp; Keep improving</div></div>', unsafe_allow_html=True)

language_csv = os.path.join("static", "data.csv")
language_data = pd.read_csv(language_csv)
with st.expander("View my current learning snapshot"):
	st.dataframe(language_data, use_container_width=True, hide_index=True)

st.markdown(
	"""
	<div class="contact" id="contact">
		<div><h2>Let's build something.</h2><p>Have an idea, question, or opportunity?</p></div>
		<a href="mailto:cyrus.bayquen@example.com">GET IN TOUCH ↗</a>
	</div>
	<div class="footer">© 2026 CYRUS BAYQUEN <span style="float:right">MADE WITH PYTHON + STREAMLIT</span></div>
	""",
	unsafe_allow_html=True,
)