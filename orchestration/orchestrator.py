from AGENTS import scope_agent,recon_agent,validation_agent,risk_agent,reporting_agent
def run(ctx):
    if not ctx.get('authorized'): return [{'status':'blocked','reason':'authorization required'}]
    return [a.run(ctx) for a in [scope_agent,recon_agent,validation_agent,risk_agent,reporting_agent]]
