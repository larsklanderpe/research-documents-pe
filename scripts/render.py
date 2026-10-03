from pathlib import Path
import base64,html,json
root=Path(__file__).resolve().parents[1]
out=root/'site';out.mkdir(exist_ok=True)
guides=[json.loads(f.read_text(encoding='utf-8')) for f in sorted((root/'content').glob('*.json'))]
style=(root/'scripts/style.css').read_text(encoding='utf-8')
logo=base64.b64encode((root/'scripts/logo.png').read_bytes()).decode()
esc=html.escape
for g in guides:
    if g.get("comparison"):
        g["intro"] = g["intro"]
    url='https://www.youtube.com/watch?v='+g['video']
    body=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{g['title']} | Practical guide</title><style>{style}</style></head><body><main><header><img alt="Player Elite" src="data:image/png;base64,{logo}"><div><b>PLAYER ELITE, PLY, LTD.</b><br><span class="tag">Personal working guide / {g['date']}</span></div></header><h1>{g['title']}</h1><p class="muted">{g['subtitle']}</p><nav><a href="index.html">Research library</a><a href="#actions">Action checklist</a><a href="#prompts">Setup prompts</a><a href="#watch">15-minute viewing route</a><a href="#materials">Materials</a><a href="{g['other']}">Related guide</a><button onclick="window.print()">Print / save PDF</button></nav><p>{g['intro']}</p><p class="callout"><b>How to use this guide:</b> choose one workflow, supply its sources and an example output, run it once, then refine it before scheduling. These are configuration proposals; nothing has been changed in your accounts.</p><h2 id="actions">Action checklist</h2><p class="savehint">Checks and notes are saved in this browser when local storage is available. To carry your completed checklist to another device, print or save a PDF.</p>'''
    for i,(title,setup,value) in enumerate(g['actions']):
        body+=f'<article><label><input type="checkbox" data-save="check-{i}"><div><h3>{esc(title)}</h3><p>{esc(setup)}</p><small>{esc(value)}</small></div></label></article>'
    if g.get('comparison'):
        table='<h2 id="comparison">The 12 use cases at a glance</h2><p>Presenter preferences, not independently verified benchmark results.</p><table><thead><tr><th>Use case</th><th>His preference</th><th>Practical lesson</th></tr></thead><tbody>'
        for task,choice,lesson,seconds in g['comparison']:
            table+=f'<tr><td><a href="{url}&amp;t={seconds}s">{esc(task)}</a></td><td>{esc(choice)}</td><td>{esc(lesson)}</td></tr>'
        table+='</tbody></table>'
        body=body.replace('<h2 id="actions">',table+'<h2 id="actions">',1)
    body+='<h2 id="prompts">Ready-to-use prompts</h2><p>Original prompts adapted for your work. Replace placeholders and provide the source documents before use.</p>'
    for title,prompt in g['prompts']:
        body+=f'<article><h3>{esc(title)}</h3><pre>{esc(prompt)}</pre></article>'
    body+='<h2 id="watch">Your approximately 15-minute viewing route</h2><table><thead><tr><th>Segment</th><th>What to look for</th></tr></thead><tbody>'
    for span,seconds,topic in g['times']:
        body+=f'<tr><td><a href="{url}&amp;t={seconds}s">{span}</a></td><td>{topic}</td></tr>'
    body+='</tbody></table><h2 id="materials">Their materials and references</h2>'
    for title,link,note in g['materials']:
        body+=f'<p><b>{f"<a href={esc(link)}>{esc(title)}</a>" if link else esc(title)}</b><br>{esc(note)}</p>'
    body+=f'<h2>Evidence and limits</h2><p>{esc(g["limits"])}</p><p>Based on the full auto-generated caption track and expanded video description of <a href="{url}">{g["title"]}</a>. Names and technical terms may contain transcription errors. The PE applications and example prompts are our synthesis, not quotations or downloadable presenter materials. This guide does not reproduce the transcript or slides.</p><h2>Your next step and notes</h2><textarea aria-label="Your next step and notes" data-save="notes" placeholder="Workflow to try, sources to supply, useful results, and corrections..."></textarea><p id="status" class="muted" role="status"></p><footer>Player Elite | Personal working guide | Source-linked research synthesis<br>Self-contained HTML: content works offline; source and video links require internet access.</footer></main><script>const key="pe-guide-{g["slug"]}:";for(const el of document.querySelectorAll("[data-save]")){{try{{const value=localStorage.getItem(key+el.dataset.save);if(el.type==="checkbox")el.checked=value==="true";else el.value=value||""}}catch(e){{document.getElementById("status").textContent="Browser storage is unavailable. Print or save a PDF to preserve your notes."}}el.addEventListener("input",()=>{{try{{localStorage.setItem(key+el.dataset.save,el.type==="checkbox"?String(el.checked):el.value);document.getElementById("status").textContent="Saved in this browser."}}catch(e){{document.getElementById("status").textContent="Unable to save locally. Print or save a PDF to preserve your notes."}}}})}}window.addEventListener("beforeprint",()=>{{for(const el of document.querySelectorAll("textarea")){{el.style.height="auto";el.style.height=el.scrollHeight+"px"}}}});</script></body></html>'
    assert '\u2014' not in body and '\u2013' not in body
    (out/(g['slug']+'.html')).write_text(body,encoding='utf-8')
print(f'Rendered {len(guides)} guides.')

cards=''.join(f'<article><h2><a href="{esc(g["slug"])}.html">{esc(g["title"])}</a></h2><p>{esc(g["subtitle"])}</p><small>{esc(g["date"])}</small></article>' for g in guides)
(out/'index.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research documents | Player Elite</title><style>{style}</style></head><body><main><header><img alt="Player Elite" src="data:image/png;base64,{logo}"><div><b>PLAYER ELITE, PLY, LTD.</b><br>Research documents</div></header><h1>Useful ideas, ready to apply</h1><p>Source-linked guides with practical actions, setup prompts, and the sections worth watching.</p>{cards}<footer>Original summaries of public source material. Checklists and notes stay in your browser.</footer></main></body></html>',encoding='utf-8')
(out/'.nojekyll').touch()

