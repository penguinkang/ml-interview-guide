from pathlib import Path
source=Path('outputs/ML-Interview-Study-Guide.html').read_text()
script='''
const remoteNotice=document.createElement('p');remoteNotice.className='note';remoteNotice.textContent='온라인 복습판 · 저장된 정답·해설, 퀴즈, 학습 체크를 사용할 수 있습니다. Python 실행과 Qwen 힌트·채점은 Mac의 로컬 가이드에서 제공됩니다. 학습 기록과 작성한 답변은 현재 브라우저에만 저장되며 기기 간 동기화되지 않습니다.';document.querySelector('.hero').append(remoteNotice);
document.querySelectorAll('.run-code,.ask-coach,.ask-grade,[data-mode="explain"],[data-mode="feedback"],[data-mode="grade"]').forEach(b=>{b.disabled=true;b.title='Mac 로컬 가이드에서 사용 가능합니다.';});
document.querySelectorAll('.code-pad>.study-note').forEach(n=>{if(n.textContent.includes('이 Mac의 Python'))n.textContent='온라인 코드 노트 · 입력 내용은 현재 브라우저에 저장됩니다. 정답·해설은 즉시 볼 수 있습니다. 실행·AI 힌트·채점은 로컬 가이드에서 사용하세요.';});
'''
source=source.replace('</script></body>',script+'</script></body>')
Path('site').mkdir(exist_ok=True)
Path('site/index.html').write_text(source)
