import base64
import os

import pandas as pd
import streamlit as st


st.set_page_config(
	page_title="Cyrus Bayquen | Aspiring Software Engineer",
	page_icon="CB",
	layout="wide",
	initial_sidebar_state="collapsed",
)

st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');

	:root {
		--paper: #0d1117;
		--ink: #f2f5f8;
		--muted: #9aa6b2;
		--blue: #6ea8fe;
		--yellow: #f3ca42;
		--line: #2a3542;
		--white: #151c24;
	}
	.stApp { background: var(--paper); color: var(--ink); }
	[data-testid="stHeader"] { background: rgba(13, 17, 23, 0.86); }
	.block-container { max-width: 1160px; padding: 2rem 3rem 4rem; }
	.mono, code, .eyebrow { font-family: 'DM Mono', monospace; }
	.eyebrow { color: var(--blue); font-size: .74rem; letter-spacing: .09em; text-transform: uppercase; }
	.topbar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--line); padding-bottom: 1.2rem; margin-bottom: 3.6rem; }
	.brand { font: 700 1.15rem 'Space Grotesk', sans-serif; letter-spacing: -.04em; }
	.brand span { color: var(--blue); }
	.nav-links { display: flex; gap: 1.2rem; }
	.nav-links a { color: var(--muted); font: .72rem 'DM Mono', monospace; text-decoration: none; }
	.nav-links a:hover { color: var(--blue); }
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
	.project-logo-wrap { height: 105px; margin: -1rem -1rem 1rem; overflow: hidden; }
	.project-logo { height: 100%; object-fit: contain; transform: scale(1); transition: transform .3s ease; width: 100%; }
	.project:hover .project-logo { transform: scale(1.08); }
	.project h3 a { color: inherit; text-decoration: none; }
	.project-hint { color: var(--muted); font: .68rem 'DM Mono', monospace; margin: -.35rem 0 1rem; }
	.project-index { color: var(--blue); font: .75rem 'DM Mono', monospace; }
	.project h3 { font: 600 1.45rem 'Space Grotesk', sans-serif; letter-spacing: -.04em; margin: 2.8rem 0 .7rem; }
	.project p { color: var(--muted); line-height: 1.5; margin-bottom: 1.4rem; }
	.tag { color: #c8dcff; background: #1d355d; display: inline-block; font: .68rem 'DM Mono', monospace; margin: .18rem .2rem 0 0; padding: .38rem .55rem; }
	.about-copy { color: var(--muted); font: 1.15rem/1.65 'Space Grotesk', sans-serif; max-width: 620px; }
	.about-copy em { color: var(--blue); font-style: normal; }
	.facts { border-left: 2px solid var(--yellow); padding-left: 1.2rem; color: var(--muted); font: .82rem/2 'DM Mono', monospace; }
	.facts b { color: var(--ink); font-weight: 500; }
	.contact { background: var(--blue); color: white; padding: 2.1rem 2.3rem; margin-top: 6rem; display: flex; justify-content: space-between; align-items: center; gap: 2rem; }
	.contact h2 { color: white; }
	.contact p { color: #cbdcff; margin: .5rem 0 0; }
	.contact a { color: var(--ink); background: var(--yellow); font: 500 .8rem 'DM Mono', monospace; padding: .8rem 1rem; text-decoration: none; white-space: nowrap; }
	.contact .nav-links { flex-wrap: wrap; justify-content: flex-end; }
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
		<div class="nav-links"><a href="https://github.com/itsamecycy" target="_blank">GITHUB ↗</a><a href="mailto:cyrusbayquen22@gmail.com">EMAIL ↗</a></div>
	</div>
	<div class="hero-copy">
		<div class="eyebrow">Aspiring software engineer</div>
		<h1>Cyrus<br>Bayquen<span style="color:#1459e6">.</span></h1>
		<p>I am learning to turn curious questions into <strong>useful, thoughtful software.</strong> This is a small collection of what I am building, studying, and exploring as I grow toward software engineering.</p>
	</div>
	""",
	unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.05, 1], gap="large")
with hero_left:
	st.markdown(
		"""
		<div class="facts" style="margin-top:2rem">
			<div><b>FOCUS</b>&nbsp;&nbsp; Python · software · data</div>
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
logo_path = os.path.join("static", "pirate_adventure_logo.png")
with open(logo_path, "rb") as logo_file:
	logo_src = "data:image/png;base64," + base64.b64encode(logo_file.read()).decode("ascii")
projects = [
	("01", "Grand Line", "A pirate adventure game based on the Pirates of the Caribbean franchise with pokémon mechanics. Built with python and pygame.", ["Python", "Pygame"], "https://github.com/itsamecycy/Pirate_Adventure", logo_src),
	("02", "HIT", "A 3d shooting game built with c++ and raylib. Currently in development.", ["C/C++", "Raylib"], "https://github.com/itsamecycy/HIT", None),
	("03", "Next experiment", "A space reserved for the next idea: small in scope, useful in practice, and shipped with care.", ["Learning", "Building", "Iteration"], None, None),
]
for column, (index, title, description, tags, url, logo) in zip(project_columns, projects):
	with column:
		tag_markup = "".join(f'<span class="tag">{tag}</span>' for tag in tags)
		title_markup = f'<a href="{url}" target="_blank">{title}</a>' if url else title
		hint_markup = '<div class="project-hint">Click title to view repo ↗</div>' if url else ''
		logo_markup = f'<div class="project-logo-wrap"><img class="project-logo" src="{logo}" alt="{title} logo"></div>' if logo else ''
		project_markup = f'<div class="project">{logo_markup}<div class="project-index">{index} — 2026</div><h3>{title_markup}</h3>{hint_markup}<p>{description}</p>{tag_markup}</div>'
		st.markdown(project_markup, unsafe_allow_html=True)

st.markdown('<div class="section" id="about"><div class="section-title"><h2>A little about me</h2><span class="number">02 / ABOUT</span></div></div>', unsafe_allow_html=True)
about_left, about_right = st.columns([1.3, .7], gap="large")

with about_left:
	st.markdown('<div class="about-copy">I am an aspiring software engineer who enjoys the moment an idea becomes something you can click, test, and improve. I am currently deepening my foundations in <em>Python</em>, exploring data, and practicing how to make software feel clear and human.</div>', unsafe_allow_html=True)
with about_right:
	st.markdown('<div class="facts"><div><b>01</b>&nbsp; Stay curious</div><div><b>02</b>&nbsp; Make it useful</div><div><b>03</b>&nbsp; Keep improving</div></div>', unsafe_allow_html=True)

language_csv = os.path.join("static", "data.csv")
language_data = pd.read_csv(language_csv)
with st.expander("View my current learning snapshot"):
	st.dataframe(language_data, use_container_width=True, hide_index=True)

st.markdown('<div class="section" id="achievements"><div class="section-title"><h2>Achievements</h2><span class="number">03 / CERTIFICATES</span></div></div>', unsafe_allow_html=True)
certificates = [
	("Python Certificate", os.path.join("static", "Python_cert.pdf")),
	("Cybersecurity Certificate", os.path.join("static", "cybersecurity_cert.pdf")),
]
for title, certificate_path in certificates:
	with st.expander(title):
		with open(certificate_path, "rb") as certificate_file:
			st.pdf(certificate_file.read(), height=700)

st.markdown(
	"""
	<div class="contact" id="contact">
		<div><h2>Let's build something.</h2><p>Have an idea, question, or opportunity?</p></div>
		<div class="nav-links"><a href="https://github.com/itsamecycy" target="_blank">GITHUB ↗</a><a href="mailto:cyrusbayquen22@gmail.com">cyrusbayquen22@gmail.com ↗</a></div>
	</div>
	<div class="footer">© 2026 CYRUS BAYQUEN <span style="float:right">MADE WITH PYTHON + STREAMLIT</span></div>
	""",
	unsafe_allow_html=True,
)

#https://github.com/itsamecycy/Pirate_Adventure

