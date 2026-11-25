from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=b.new_page(viewport={'width':1200,'height':1000}); errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
 page.set_content((Path(__file__).resolve().parents[1]/'index.html').read_text())
 for case,expected in [('normal','Rising distress'),('failure','Prediction mismatch'),('recovery','Falling indicators'),('missing','Interrupted audio')]:
  page.select_option('#scenario',case); initial=page.locator('#score').inner_text();page.click('#next')
  if case=='missing': assert page.locator('#score').inner_text()=='Withheld';assert 'No usable audio' in page.locator('#warning').inner_text()
  page.click('#next')
  if case=='failure': assert 'Low confidence' in page.locator('#warning').inner_text();page.click('#clarify');assert 'angry' in page.locator('#reply').inner_text();page.select_option('#observation',label='Possible frustration');page.click('#correct');assert 'Possible fear' in page.locator('#log').inner_text()
  page.click('#next'); final=page.locator('#score').inner_text();page.click('#next');assert expected in page.locator('#summary').inner_text(); assert page.locator('#reviewRows tr').count()==4
  print(f'PASS {case}: {initial} -> {final}; {expected}')
  with page.expect_download() as d: page.click('#export')
  import json
  export=json.loads(Path(d.value.path()).read_text());assert export['simulation'] and export['scenario']==case and expected in export['outcome']
  page.screenshot(path=str(Path(__file__).resolve().parents[1]/'storyboards'/f'{case}.png'),full_page=True)
 page.click('#reset');assert not page.locator('#review').is_visible();assert not errors,errors;print('PASS all four JSON exports, reset, no JavaScript errors');b.close()
