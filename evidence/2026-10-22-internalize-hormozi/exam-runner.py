from pathlib import Path
import os,subprocess,json,runpy,sys,time,hashlib
root=Path('/Users/wendy/work/park-knowledge'); ev=root/'evidence/2026-10-22-internalize-hormozi'
runtime=root/'.internalize-hormozi/claude-runtime'
runtime.mkdir(parents=True,exist_ok=True)
if not (runtime/'skills').exists(): (runtime/'skills').symlink_to('/Users/wendy/.claude/skills',target_is_directory=True)
real_run=subprocess.run
credential=real_run(['security','find-generic-password','-a',os.environ.get('USER','wendy'),'-s','Claude Code-credentials','-w'],capture_output=True,text=True,check=True)
token=json.loads(credential.stdout)['claudeAiOauth']['accessToken']
env=os.environ.copy();env.update({'CLAUDE_CONFIG_DIR':str(root/'.internalize-hormozi/claude-runtime'),'CLAUDE_CODE_OAUTH_TOKEN':token,'DISABLE_AUTOUPDATER':'1','DISABLE_TELEMETRY':'1'})
results=[]
def logged_run(args,*a,**kw):
    if args[0]!='claude':return real_run(args,*a,**kw)
    cmd=['/Users/wendy/.local/bin/claude',*args[1:],'--no-session-persistence','--tools','Skill,Read','--allowedTools','Skill,Read','--permission-mode','dontAsk','--setting-sources','project']
    kw['cwd']=str(root);kw['env']=env
    start=time.monotonic();out=real_run(cmd,*a,**kw);events=[];called=[]
    for line in out.stdout.splitlines():
        try:e=json.loads(line)
        except ValueError:continue
        events.append(e)
        if e.get('type')=='assistant':
            called.extend(b.get('input',{}).get('skill','') for b in e['message'].get('content',[]) if b.get('type')=='tool_use' and b.get('name')=='Skill')
    final=next((e for e in reversed(events) if e.get('type')=='result'),{})
    valid=out.returncode==0 and final.get('is_error') is False and final.get('subtype')=='success'
    rec={'prompt':args[2],'exit_code':out.returncode,'elapsed_seconds':round(time.monotonic()-start,2),'result_is_error':final.get('is_error'),'subtype':final.get('subtype'),'skills_called':called,'valid':valid}
    results.append(rec)
    with (ev/'exam-sessions.jsonl').open('a') as f:f.write(json.dumps({'receipt':rec,'events':events,'stderr':out.stderr},ensure_ascii=False)+'\n')
    print('session',len(results),json.dumps(rec,ensure_ascii=False),flush=True)
    if not valid:raise RuntimeError('Invalid CLI session; cannot score as passed')
    return out
subprocess.run=logged_run
sys.argv=[str(root/'bin/exam'),'know-offer-pricing']
try:
    runpy.run_path(str(root/'bin/exam'),run_name='__main__')
finally:
    (ev/'exam-session-summary.json').write_text(json.dumps({'runner':'bin/exam unmodified via runpy; new CLI processes use project cwd, isolated runtime and read-only tools; no prompt or scoring edits','exam_script_sha256':hashlib.sha256((root/'bin/exam').read_bytes()).hexdigest(),'sessions':results},ensure_ascii=False,indent=2)+'\n')
