opers="""
plus:+
minus:-
multiply:*
divide://
logarithm:math.log
pi:math.pi
power:**
point,dot:.
square:**0.5
open:(
close:)
"""
sys_info.expr=[]

kws={
  'equal, result':calculate(),
  'home':say('back to boot') & mind('boot'),
  'quit':quit_app()
}

sys_info.calc_opers=_lines_to_dict(opers)
kws.update(_lines_to_dict(_fread('nums'), add2expr))
kws.update(_lines_to_dict(opers,add2expr))
