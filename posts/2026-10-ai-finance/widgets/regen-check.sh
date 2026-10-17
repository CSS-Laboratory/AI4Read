#!/bin/bash
# Regenerates check-output.txt for post 02 widgets. Run from this folder.
C=/home/claude/ai4read/site/ai4read/components/check.mjs
{
echo "# check.mjs readouts for post 02 widgets"
for f in w5-cascade.json herding.json labs.json ashby-stepper.json w5-hand-stepper.json; do echo; echo "## $f (default values)"; node $C $f 2>&1 | grep -E "■|readout|bars|failed by|row|OK|✗"; done
echo; echo "## W5 cascade, seeds"
for s in X1 X2 X3 Y1 Y2 Y3 X1,X2 X1,X3 X2,X3 X1,X2,X3; do echo "seeds $s:"; node $C w5-cascade.json --seeds $s | grep -E "readout|failed by"; done
echo "seeds X1,X2,X3 capMult 1.5:"; node $C w5-cascade.json --seeds X1,X2,X3 --values '{"capMult":1.5}' | grep -E "readout|failed by"
for c in 1.2 1.25; do echo "seeds X1,X2,X3 capMult $c:"; node $C w5-cascade.json --seeds X1,X2,X3 --values "{\"capMult\":$c}" | grep -E "readout"; done
echo "lgd=1, seed Y1:"; node $C w5-cascade.json --seeds Y1 --values '{"lgd":1}' | grep -E "readout|failed by"
echo "lgd=1, seeds X1,X2:"; node $C w5-cascade.json --seeds X1,X2 --values '{"lgd":1}' | grep -E "readout|failed by"
echo; echo "## herding (--values)"
for v in '{"m":0.2}' '{"m":0.67}' '{"m":0.9}' '{"m":0.9,"brk":3}'; do echo "values $v:"; node $C herding.json --values "$v" | grep readout; done
echo; echo "## labs (--values)"
for pair in 'cfg-cdo|{"p":0.1,"w":0}' 'cfg-cdo|{"p":0.1,"w":0.5}' 'cfg-cdo|{"p":0.1,"w":1}' 'cfg-cdo|{"p":0.02,"w":1}' 'cfg-count|{"k":6,"d":1}' 'cfg-count|{"k":10,"d":1}' 'cfg-count|{"k":14,"d":1}' 'cfg-count|{"k":20,"d":2}' 'cfg-ashby|{"c":4,"vr":4}' 'cfg-ashby|{"c":2,"vr":4}' 'cfg-ashby|{"c":4,"vr":9}' 'cfg-ashby|{"c":2,"vr":9}' 'cfg-neff|{"N":10,"rho":0}' 'cfg-neff|{"N":10,"rho":0.3}' 'cfg-neff|{"N":10,"rho":0.9}' 'cfg-neff|{"N":10,"rho":1}' 'cfg-neff|{"N":100,"rho":0.3}' 'cfg-bayes2|{"n":0}' 'cfg-bayes2|{"n":1}' 'cfg-bayes2|{"n":2}' 'cfg-bayes2|{"n":3}' 'cfg-bayes2|{"n":4}' 'cfg-bayes2|{"n":10}'; do id=${pair%%|*}; v=${pair#*|}; echo "$id $v:"; node $C labs.json --id $id --values "$v" | grep readout; done
} > check-output.txt 2>&1
