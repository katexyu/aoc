from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

actual = """
qzbs: 3
wljg: 12
zgnc: dmcb * wlvd
vrzg: nczp * qfdp
zpvn: twgm + nbbw
jdtl: 5
nrsh: vjtq * zwvv
tpjl: zgpw * mcpf
root: rjmz + nfct
bjnf: czsb / spcv
ngpw: 14
qpvs: 9
tlvh: ztcd * nftj
srtz: mhld * qlhg
bjhm: 19
bfjr: rhzr + tqqh
vgnh: 2
fqsd: hsml * wgrl
bjmm: 4
gdvj: 3
cmzb: 9
vrss: 2
gcnd: nqjd + zlzz
mzrp: 5
blsc: dgss + qngp
pvzf: 6
cfmn: 4
gvqz: 17
wzgd: 2
ljsh: bqgd * jhwd
szgz: thvw + lfsz
wzpp: 3
dhgt: 2
rtlb: 6
ptfc: cgcz + mrrc
ddpj: 5
nvht: 2
bvdf: 3
mqvp: 2
vjcb: 10
rwcp: gmlr - lqvq
pdnz: 3
cpnv: sqgz * sfdr
cdrn: srjj / frzm
lszf: 3
gsvr: mrnv + ddwn
nrwm: wvpv * rllz
fbjd: 2
cdvp: 9
mfsr: rbmc + ngvs
dzhr: ttzb * tpml
tnql: 4
fjhm: 2
mvww: gpqt / mplm
jzfm: frmc * cnbm
lsfr: gcjr + fcqp
nrcb: gvzv * gzvc
jdnb: 17
lvpp: 5
gvts: 13
nhnb: 7
fbgr: 4
zsdm: nrsh + vwmz
lmvh: pdts / wtrb
sjls: rcfs * nvzq
qfvh: 5
qjdg: hfcs * lqgf
djcv: 5
fvlz: 2
bjrw: vdhz * cjgv
lcqw: 2
wtls: 2
pwwf: zppz + vvhp
hmst: 3
ctsd: hdtq - dsww
ldrt: vmfg * zztt
ncph: sgss * sfgv
ndzr: cqvh * gvts
zwzc: zrhs * drls
lnwc: 1
gmhv: tqtw + qpwl
srws: 2
wpzf: zltf + pjww
jrpb: tjns + tpjl
blcq: pjgp * dptw
zlql: 4
hgbc: 5
zwqh: wllj * splp
trdh: pvdc - crqs
hlgm: cfqs + sqcz
gqvl: rvqw + gsqb
vzvc: 2
dtqg: 12
dcst: rgmz * bpsr
gjbn: nrwm * mbqq
nnpt: vjtv * zvjf
zqgt: vdln / blwf
pqsz: 6
gfbw: 1
zpfn: rbmv + zsrn
qrgb: wcbw + fjzb
qmjg: 2
nmmg: 17
jmqf: 2
nltr: fwmw / wmzm
rjhv: bhjc * tpzv
gbzg: trdh * prfb
qwrd: 3
jtvf: sghw + fwfr
clhn: sznm * fwgn
brnc: 2
sssf: 3
njpz: 4
tcjb: 2
fbvz: dshj * rjjc
pzrj: 3
qhqd: zzwf * cghd
vmfg: 3
snmh: gvhv * cfws
bhvd: 2
lvgh: vnzd * dpbl
pmcz: vgnh * hwfh
rshf: tlfd + tghs
hlqt: pjth * svcl
hfjh: 2
sdlh: 10
rcjj: 5
rrws: zfcd * bcrl
sznt: nbcn * dcmj
fgqs: zrml * fvwv
jmtw: wtcw / lbzv
twzv: rtpq + brhz
rrts: fvtj + wbrd
jrcc: 3
bccm: 7
vwht: 2
mwzp: pwpp + vjdv
chmw: ptsn * qhbr
gzlv: 2
cnch: 3
qhzj: 7
mslt: ffgc + tfwq
lfjr: sjrn + vhmn
nznf: 2
mntq: 18
dvvl: 2
pjww: bjfb * cfzl
vnbg: rdzd * lbqr
rwqw: vvdw + scvr
nfld: 9
vnpt: 2
dlml: 2
zsmt: 15
mftl: bpll - rrwn
hhgl: zmrz * wfsg
vbfp: bjht - mprq
lwrg: phjf * swsb
zdqn: 11
dmqh: 3
qddl: qmcl + srhq
ddpw: 3
lbdb: qbjb * rmpt
sqrs: 3
vrfm: 2
ljwh: 3
mvqw: 5
mqhc: 5
mrrd: 3
qrfg: 2
vqmw: 5
twfz: 5
pmlt: wsbc * rlch
nmpv: qsps + cmrn
gsrb: ctrs + mzrp
rggn: 2
jpbc: 3
pmms: 2
blbj: szbl / ltwg
rghn: 10
bbnv: 2
qwtb: 3
cbqz: mbgf + jwrs
gqms: 1
rrqq: gptp + fsdc
jptq: 4
dgwp: 2
ghcz: 10
ggrl: 5
zwjz: hhhs * fbtd
zrbm: 2
qdll: prdt / nsvj
frzm: 2
cgzr: 2
fqdw: 3
cbwv: 3
gvdc: rrzw * sbsd
mzvr: 8
jgqw: 1
hbbr: 5
lrhn: 3
mmlq: 1
nmtm: 2
tcfm: 5
bfjm: vqnz * zcrf
ldnh: 2
qwlc: ptjs / bbrs
zqfq: 2
rmpl: qgwb * rznj
qvgw: dlzw * vbzc
lpct: 2
zvnz: 2
zhhc: 4
gdgl: 10
fnln: 2
fssl: 2
gptp: cpnv * tzcs
gvsw: jpvw * mgcq
srct: zngs + twzv
cvrw: rmpl + qlpg
fzlj: 1
tfvp: 6
cgcs: 20
fqcf: 3
dwvh: whsr * bcqh
wmqr: 2
gldv: rjzq + qjjh
cmrn: 11
wsbc: 5
qctc: 2
qfcr: 5
zqmj: jpjc * nhgm
vlfp: cblm + tssc
ftst: fnhd * ptjj
zhvh: rqdr * vdgf
wnbr: 4
lhvh: 3
zlnl: 3
vzdz: 3
gvnr: 1
wwfg: 1
tntz: gsrb * ftmd
dllm: mqng * jtst
mrpp: fnws + zlbt
wrnj: zqlm + pbjl
rhjg: pwnz - tgrc
fsgj: czgl * bjrw
nlrl: 12
ngsn: 3
frmc: 2
mmpp: 9
dlmd: 5
trsm: 2
wntt: 2
rllz: tdnh * dhwq
clgs: 2
zsvv: 2
zhfn: nwhz / hldm
bjlq: dtlc / pvzf
gwvr: ctvh * rslf
nrww: 16
vlqf: cvcn * vwvp
nhpf: 2
cptf: 7
fpzv: 2
ttnr: 4
vqqg: jdqv + lslb
tghs: jdhv * vjwj
fjdj: qpmg + zhbm
pzlm: 8
mhhl: 2
hlrg: 2
wnjm: 4
jfrr: 3
jljq: 2
sfnf: 4
qrvp: rhqz * jrpb
jrhz: 4
mwls: ngsn * rsrg
tjvp: qzcs * wrmp
qggh: dmqh * ltvs
jdhv: mmsb + ndsj
jdmj: 3
gzvc: ptgh / ssql
rzlw: dnqp + rzpq
pnps: 5
fvbc: swsw * fcvp
rpsn: vdtg / flpl
drrl: 2
mzvj: jnhb + rjsr
qzjb: ftng + btmj
gznz: jrjg + njbj
cqtl: 5
zlrz: 7
pwng: hgwq + jmst
dmgm: 2
ghsh: qssg * bfqz
vtwn: 3
dvms: lhlr + dsrm
qlfp: mwgw * cdvp
ngvs: pcgv * qsnw
ztlf: ffrr * ltgr
cwff: bbpq * hrrs
qzcs: blct * vjzc
lszs: 1
vmmj: qbww + fqvz
jtlr: 2
mflg: 2
wscg: cbnd * mqwl
rhdd: pdtt * rrts
ghnv: bscd - pvpf
vcdh: hlgm - tmpn
dsvh: fqcf * gtwb
tqrh: 1
nhgb: 3
pnff: 3
mtld: 3
qlrz: bwbn * lvpp
mtrp: lhtp / wzgd
trct: 4
qbqw: 2
pbdh: 6
rqbc: 5
chjg: hqlj - dwmr
pjth: 5
cdzb: 2
vqnz: 2
bbtm: frfc * mdtn
mszw: 4
lcdw: 18
smdv: 5
bdsb: tttd + qlrs
gqgp: 2
vgnb: gsdv + fcsw
wqcq: 4
vtlp: 4
lfcq: cfqq / rdjb
tbbf: lcqw * wjfz
fdrj: 2
vrrq: jljb * ndbj
clbn: tncs * tctb
gwcg: cbwv * lvlw
gdds: nnpt - bqvq
prbd: 2
mqng: 9
tbnj: nwvr * fpzv
nwsb: nlqc + hdhb
tvhp: gzgh * vltr
njdf: dbzv / rvls
nnhg: pgtq * tlvh
lccj: 3
zppz: 3
qvjm: ggcg + wpmp
jgqf: rmvd * lnbj
jwdr: fnjs + lwgc
wvfm: wnfl * nnmp
hqzd: 17
lfsz: 20
lgwb: tngd + trlw
pdbh: 2
brbw: zllr / sgng
wdng: 4
ltjc: 7
czdq: 9
mfvq: 2
jvqv: 2
mrwm: nqsg + psnf
zcnm: 2
hvfh: ncft + zlvn
fcbv: 4
jcpw: vcvr * dhgt
zvzh: 5
jhpz: nmtm * rpzb
bmzs: 9
vgnd: vnmq * rcdb
przl: 13
pfdj: vrcw * rzlw
slcw: 4
slrc: rlqz - djcv
ppsv: wmqr * zjsh
twpq: hqdl * bmtc
rcqv: hbvw + qpsv
dzgz: hcvc / lvwj
plpz: 3
rbjm: fqst * vnrq
qvpv: 5
gssd: zcct * nrjs
swpr: 3
vgsm: jpwf * dpsf
msgg: 2
lvmc: vmzt * jjwm
gmlr: 8
tmbs: 3
hhhs: plpz * tchp
mdps: 2
lmqp: 6
prwc: 2
dqqh: 5
mmnm: 2
szbl: jzms * cgzr
dqgd: 3
rtzh: rqjz + tfgb
bscd: ppsv * cdgj
wzhd: mlbn + qlrz
qjhv: 10
qlnb: 2
pjqr: thwh * jblq
lwgc: 4
ttds: jvfr * hgmz
qpjs: jcgp * sjpd
mlpm: 3
qvmf: 2
dhwq: 2
ltsj: 3
qchm: 3
vrrt: rfdq * fzlw
sbrm: pjbq * zlmh
qvcv: bblj + vwzq
cwrs: 5
gbtv: 11
fnjs: 17
pmvp: ndbl + qjdf
vzcb: 10
swwz: gzsl + vplh
csgg: sccr * frwd
tnjc: bsmc * nvrj
qtls: jwsq * zzbp
brms: 11
qpdt: thjc / qzps
fqvz: lnbb / ngjw
dcmj: 3
lwwg: 2
cvjw: 2
wmdv: 4
mcnn: 3
lqjq: 7
wnsj: pcch * sqlq
snqn: 3
prfb: 2
hlqg: wwft * mvrz
cbnd: dslw / pdbh
rnsz: wzzj * bsnf
rjzq: czrg + zdvl
dpbl: 3
nnvf: 5
wgzq: 2
rrzw: 4
cqfb: 4
gzgh: zrlr * zrww
jrjg: llmm * nnqr
vrfz: 4
qlrs: 8
hdpw: bzdn + trhd
qdlz: rrnv / qbnf
mpzw: 2
zztt: 2
jgvd: fncw / qcbt
phjf: 2
jltr: 15
qzgp: 2
rbdm: 8
wjgt: cnpj * jjrp
hmcb: dfcf * swlf
mcpf: 10
shhq: 5
jgdn: 5
smdr: rpsn * cnch
wtzt: 3
stcr: jbtq + cbgp
hmsw: 5
qcbt: 3
mvrz: rbbm / pdtd
frng: 2
zztp: 3
vnrq: lhvh + zgpz
vbhp: dpdd + wlqn
dlbq: 10
qtbp: jfbg * hpdd
qjpj: qpdt - wpdc
grjs: qcfz * nnqn
qcjb: gzch + sftz
hcvg: hwqf * sssf
cfws: 3
gzgg: 3
jpld: qwlc - qvpv
bdwp: 3
fqjn: gmdl + csdm
ctvh: 7
dfqj: hzlp * zvzh
tfnh: 4
dbzv: pgnc * nfsn
pgmh: 2
mthd: 4
qgpl: qjdg + ghsh
drvz: 4
rsrg: wqcq + rgfd
dttf: fwtj - qcbf
rhzr: 1
wstn: qmnf * vtlp
nccr: 1
zqvs: 2
sngh: lgnb * hmhs
mrgf: 5
qbvl: vvwz * vvdm
qtnm: 3
cpgn: 7
qnqf: qddb + pnps
ntcl: 2
pqdv: 2
fbtd: fqbw * gtrj
tvnd: bgnt + vlqf
tdvq: 18
jvbr: 2
jsct: 4
dvzm: 2
smnt: qvmr * hwcm
cgqm: 4
vbtf: 2
sqgz: 13
dvvj: bdsb * vrls
rjbt: wczf * hztb
pvsr: 5
dqst: vgth + mhnd
jttn: mdvg * jgfq
hrnv: 4
ztgv: 3
jngv: 8
flvm: 2
bvnc: fgff * mhbj
chsz: 2
zbtd: 5
ghgm: 2
rqdr: 6
lhvv: rmfh + nnvf
mcgs: qbwm * fngz
jlfz: spzw * dpss
tqlj: zfsl * vgmd
cgjf: 5
qjsf: ddcv * hwwh
lchg: 4
hhrw: vmvg * mnbq
bshf: lgmc + gjpw
twpf: wpgt + fzdz
fngz: sznt / bwjl
fwwq: 2
bgdd: 2
nrcl: 2
sdbd: 1
mhld: mnlp / qzmr
qvjg: whdz * hznl
nlmg: crcq + cnqc
plzs: 19
dncc: cqwc / zpcp
rjmz: srpq * rvdv
dhtj: nfhr + wbfl
whsr: dtpb / rtmv
pqbw: 14
rlqz: hmst * zfdw
dtrh: 3
tpmb: 5
mtzm: mmcp * ffsh
plhd: zcpn + lnwc
zqlm: 3
tnfc: 12
pqcf: 7
dddc: ssdm - qghd
bwjl: rzjr + jlcw
gcnf: rbjm / lmdz
nshq: gfsp + crzs
cwgj: 2
tfpj: 2
bfgf: cggz / hfpf
rzpq: 2
jbjg: 2
jlcw: 5
jqms: 1
ncvd: 2
qpwl: 14
qgwb: 2
qtnj: djfz + gfsn
fjbm: lstq + vcjs
ggct: qpgr + vtbw
czhg: mrfm + wwhs
slwc: 4
njqv: 2
bcrl: 3
pzth: zwfj * jdtl
gpqt: cnpt * czhg
zhdp: cgjc - fvtz
mdmw: 7
fjfv: 8
lfdg: sdwm * htmt
nzqd: zsjp * lzwj
lbvb: wwmb * bqgc
ghtt: 6
frjs: hplr + ldrt
lhsv: 20
vtlh: 2
rvdv: rdwp - dzgz
blhh: 2
ptbs: 2
pjvp: 4
hffj: 2
tqtw: scvp + wnjm
rgbz: 5
gdhz: 12
phgr: mjqs + sjtj
qbfg: wwln * vndj
gwms: 3
jcvw: 2
dfbt: mdwz + pqfc
fftb: ttds + dljp
nfqs: lnvw * rrdb
vlrq: 2
cbtt: 2
dfvb: sbbv - djfd
dtzs: 1
bglm: tbgp * fcvc
lggn: 3
rznj: tscn + tccw
qcjj: jfqd / jvlp
mpts: 4
twnp: 2
hgrp: cgzb + ztlf
rbmv: bspb * pcbd
dwmf: fdfb * svqp
bjfb: jzws + qsbq
rfzm: 2
dptw: 5
tnnl: pvzz * gjfd
fpwv: 2
hgwq: 12
fswr: 2
hncb: 10
lphl: 5
rtbq: jpld * ddpw
jlht: 3
vbzc: grgg + fgdn
mrrc: qvjg * pqtr
mmsb: 5
sqdq: fccc + wmhp
wcqc: qtmn * gfhd
ddht: njqv * rzzs
lsjr: 1
pmbz: fmfh * ljht
cdlt: 3
gbmw: 2
rtvd: 2
jmbq: 4
rhmr: ttrm - trql
svgt: 5
ffgj: 4
qntn: 8
jcdj: 13
qwbj: dcbf / gnrv
hnbn: 3
vpcz: bshf + lfjr
thvg: 4
vzpn: 3
vplh: lfcz * wpfs
ffgc: wzpf * vtdv
dzrn: jbjg + tnfc
zqnb: djcp + hfqs
rbpd: jnzf + thww
hfdf: 2
ncwb: 2
splp: lcgg + lzdr
gtbc: 4
wlqn: 5
wdqm: 8
fdvw: 4
gtfw: 17
gcmr: dddc + nmpw
dwrd: nltr + nphz
bjpg: ldst * chsr
bbrs: 2
psdd: 5
dfjz: 7
grgt: 1
sjtp: 3
nnqr: 4
bnvs: sfds + ndfm
wcjw: rlqw * jmwn
bldf: cccl * pfwd
bmrv: 2
hfpf: 2
bbpq: 9
nvzq: 5
fwmw: bdds - blsc
pbwf: mrwm + rlqv
wbzv: 14
sbnm: twpf * cvdn
dzcm: slcw + ddgj
zvhb: smvb + dzhr
vtzb: 16
mbdv: 1
rftp: 8
wrds: blcq - mvfw
bfqz: hdmn * bgpb
lstq: pglr + wnsj
zrbb: czld * rrws
zjsc: cvrl * rtzh
qlgf: rpcn / mmnm
rwvj: zltd + ldgm
ddzb: flbs - pptn
fdmq: pqqb * swzt
qjjr: ptvc - wsjg
ndzf: vgnn + qgjs
gjcv: gwqp * ztbn
cpgj: 5
zfsb: 16
hfls: 3
ntzb: rdml + hnqb
zfrs: rwth + zzbw
dwjr: tvrs * frlq
fvtz: dddj / fmzs
dcmw: lfdg + fplh
wltl: gldn * dvcb
zfch: 2
wtcw: hspt + qrwj
mnlb: phcg + spps
jtdm: tvjz / wnvv
ttrm: rwqw + sgdt
nwhz: gppg * shjb
zscq: 3
bgqr: 3
vwqs: bwdg + nfld
cfqq: svzb * cwtt
dfgj: 2
qwbz: qbnm * djdl
qgtm: hmcn * vbtf
wtsj: 5
jgzd: dcmw * nmpv
twdn: 3
czhr: 2
bpmv: tmsg * tddw
jjpc: 3
zrmz: vtjr + zpbs
pqvw: cpdz * qfnq
vrpw: bgqr * znlj
lzgt: srjm + fhpc
ddgj: 3
vsnh: sjtp * hmtg
swsb: 4
bpwr: htzt * fsss
fbvg: 8
qjnf: 4
lgmh: 16
fvwv: 2
nclt: 5
bgsc: tpsd * qzgp
pnch: qpnh * tbcm
rvsn: btfb + dndc
sswg: frht * vjbq
zfsc: gvnr + fqbm
pgbm: pqfh + lcdw
frwd: wlsc + snjl
nqtz: 2
dwpj: pgsg - glmq
mfrh: hgmh / qdvs
fjzb: lwbt * zclj
jndb: 11
wswj: zvzw / sqrs
wtrb: 7
fcnt: pqdn * mccp
wmbc: 3
tchm: 12
qlpg: lzdt + twcj
gzgj: dncc + rjbt
qpgr: 9
nqjd: rdjm * cpwr
pmvs: 3
tgnl: 3
ljfq: 3
dvln: 6
rwgg: 2
vdqf: 3
rmmd: fhsg * qdlb
bshc: qmsz / jzqg
hspt: ncwb * trch
jblq: 3
spps: qlgf + lzcr
qvrh: 2
fqbq: 3
cjzv: jlhb * flqd
nvdj: 2
rcdb: bmgt * bltf
nczp: 2
vlbr: 3
nwzw: 17
tddq: dfgs - pwwf
fhhl: 16
vmjf: 2
hgmh: fssl * rrrz
hnvb: vlrq * gwff
tsrb: hdgc / rgbz
cqnf: 3
hnqb: scng + ftst
clpg: 3
rjpq: 3
humn: 1860
mlwf: 5
bjrh: zmcq / pdfq
mvrs: dgcv + bjfv
pfwd: fzrv + gqbt
rqld: sbnm * dcdl
hztb: hclz / wlvn
nfct: rfmc * ndsm
cggz: tzlw * jvqv
dwlm: dzvn * fvlz
cvsl: zhhc * qrdb
zsfq: 3
qmcl: frqt * rthh
pbtg: 5
wmlp: 13
sbsd: 5
wphf: bzql * slrc
slnr: qdlz * glqz
smvb: hpwq * gqmw
mlnt: pglg + sdzt
hvgm: pgvt + bvzb
bbrp: 4
gnsr: whhn / dvvl
gcds: 12
rdlb: 2
dtlc: hcrw * mqhj
dzsg: 5
mlpq: csmt + tqhw
pcbd: wwvw + bbdl
wpfs: 2
gpcd: 5
sznm: 12
wswt: mrfp + rftp
sntr: 7
cfgb: 13
rwth: jdgg * fdvw
hqln: hcsd + srtz
rlqw: dzzw + jdzb
rjjc: 3
zcdc: qqvm * srvm
vjzc: 7
smjc: 5
zgnz: 6
fqbw: 2
gvcg: 3
fcsb: zrcv + bgdd
qzbn: 12
rvcm: 2
fdvj: 5
lcjd: rfrm * pqml
jfjl: rztp + vgqd
szpr: qrvp * jchj
mvjt: 19
tjfh: tztt * shhq
cgjc: zqdb / gzjj
chsr: 3
cgsz: 11
jvlt: 2
jgbq: ngdm * jjpc
cszb: dqgd * twrw
pghq: jbrb * mthd
lvhp: vrfz * jncv
bjnd: vpsm * zscq
tqqg: 3
mgvr: 18
qvpc: 4
dljs: cfzf + nlrl
nbbw: bncf + pzhw
nbhr: 1
zqfl: 1
cszj: hlqg + fqwq
sqnz: fgjg * tbsl
qdjj: 2
sjtm: 4
hqdl: 4
ftlq: 12
fdrn: 7
bjfv: ntrv * tgvd
pcfw: pjvh - dwfg
tvsg: frqw - rggn
hcrw: dsfs * qzns
bnwl: 14
zhsd: vrpr - sswg
hcsd: ssdj * gwms
gvhz: wtwh + qzjq
gtwb: jfrr * hspg
jvfr: 3
cwmq: frfv - mpvf
pvjl: dpgm * qbqw
cvdn: 2
ndhh: bjmw + lfcq
hnpc: wfnp + pfhb
sbmq: 2
mlgb: 4
vgms: jtlr * mlzv
fsdc: grmm * smnt
qzlh: vfsc + wmdv
srzj: hqln + dlml
hbst: vccm + vcdj
tzpq: tvhq - jlht
prcd: lpqj * dwpj
bvfq: 2
tcfn: 5
ndld: 3
dpdd: 2
tzcs: vpfn * jvbr
bnzl: 1
scvp: 15
tvhq: 10
trlz: 3
grld: 19
gvtg: jgbq * fmqz
sgwv: 2
tsfb: 6
spzw: 4
vvwz: 5
lpqj: 4
zddt: jmsm + fbgr
drfv: fsgh * rtcr
cdgj: 3
jzqg: 2
chdc: rvwf + mhvf
ljht: rhcn + gntv
cpdz: bcrr - jbln
lllb: 3
hdrw: vcgd * hqfm
cbjl: tbnw + cqjp
jblc: 2
wwdw: 3
gsqb: 3
thww: 4
wcgl: cssz * bhvd
wbwd: jjgs + rlqf
hznl: gjbg + trsm
grvh: 2
djdl: 5
zmjz: 9
tlmt: 3
mjqs: gslf + mtqf
dqhl: pnch / tbhm
sgfw: jsct * fjbm
dmvw: 6
ptvc: tmsr * gwvd
qhnh: 1
sjrn: rdzq - rgml
czld: pjvp * bgwj
dgcv: zpjf * mpsz
zrrq: 5
rfgt: 3
gtrj: 4
wslc: 2
zdmm: 4
mhtf: 3
mwsv: 3
pnwd: ssqq + cfrd
nbml: 8
dvcb: sbrm - hrqc
tqwf: 2
gnqt: 12
pzhf: 5
bfpp: rvbv * lflg
ttgg: thwn / htph
rdzd: ctwv * twdn
fftm: 3
wdzv: 11
qszj: hlrt + zpqj
zfqs: 4
pscb: 2
pdbf: cnvg / pgmh
lvnl: bgnm + ddzb
lhcc: rfgt * zcvm
zsgq: ntzb + lbrz
dwvf: jbmh * npdb
gqbt: 5
mbgs: rvnw + bldf
vcjs: wbgw * nssh
pswd: 18
bmvs: cggf / tcjb
hlvv: 11
bprd: 2
gqfn: jncz / mflg
zgnr: ppml * vmvc
cdtl: qmfr * vrpt
twgc: sqnf + jddc
vgth: wsnd - vdgg
qddb: 2
mrfp: 15
mwgw: 4
qbrd: 2
mngl: 2
pcmg: 8
bzzj: zmdp * pbbs
zlvt: 13
qmvc: 6
zvzw: pdps - nzvt
zzpb: tvnz - vrzt
gsdv: wcgs + qwbj
gqgg: 2
grqd: vzpd * bhqc
wwhs: sjtm * fhgp
rvwr: 1
chmg: 9
htfv: mjpd + rvwr
qtmn: plpt / gtbc
rvzw: 5
blrc: vtnm + tjvp
qpnj: 3
wbrd: htpv * ttnr
fzdz: 2
gjdc: bsbf * jvwz
wqqc: bjmh * gcmr
qcgs: stpb + sshc
bhjc: wvzj * bbfj
bvlz: vdmj + mnlb
sbgm: ghcz + zwcv
fzns: vrss + qjrr
pdnf: nlbh + vrrq
vgqd: 10
nvrj: mgvr + cgdr
lqmd: 18
tmsr: 2
bhrr: 2
pbzc: dzdm / qhrt
jqmg: zddp + rdnd
tgvd: vcvc + vgfw
zshc: 2
hdgc: zvhb + zvmb
jlng: 16
hclm: 2
pfrh: tbbf / clqj
gzdf: 11
lwsv: 6
lvtw: mvws * sgmb
bwnn: rfhv * bbvq
cqjp: 15
zfdw: nlwc * lpct
smqd: 16
qhsv: lzrp * ddjz
qlhm: jvlt * jdmj
zfsl: 8
mrws: 2
tdbb: tmbs * qzbs
bccg: 2
pgtq: 13
vvcp: 3
vsbl: fmqf + jgpm
gntv: phlj / vcgl
lzwj: 2
frgd: qjgm * gzgj
prrw: tszg * mvpl
qngp: pfdj + wntl
wwln: gnqt + mstq
wbbd: ppqq * gdpz
htdt: 3
clqj: 2
dclr: 3
pptn: jlwt * sqhj
cvhl: wwbh * ptbs
pjdt: tfvp + sbwg
jrmj: 6
hhwj: 2
gnbc: 3
tzhz: qmjg * jstl
qpzq: zcjn / bjzw
jstl: gplj + vlbj
zbln: 3
vgcl: 1
jpwf: 2
pznp: hmcb / wtls
bmtc: gggt + gvrh
cfzf: 8
zfzv: wqqc * fwwq
pvdc: hzcl * dqhl
vdtg: glfd * mpzw
jmsm: 3
bhmg: vdqm * btjp
rvvz: dfjz + drvz
jmwn: 3
thbw: 1
vrmt: snmh - cpph
hwwh: 9
sdzm: gvsw + hqwv
zwcv: 5
zqnr: mvww * hfjh
fshr: 2
jtct: wlrg + gzlv
gvhv: bpfn / cptr
bvfh: 2
njbj: nnrg + tqdq
wnml: bfjm / zwmv
lvlw: ddpj * hclm
gfhd: jnrq + vmwr
twhm: 5
hzcl: 2
ppnc: 12
fwrq: 2
bdlf: hltp + smmd
dqrc: rcqv - sjnp
vvmp: mlhm * fjml
mfpf: 7
qhlg: wcgl + qpvn
mqrr: twgc + fmhh
djfg: 2
nvgh: 3
wwfd: 10
dqng: dlrb + pdnf
ztrv: 3
ghfv: qstl * hrvb
wsdt: bnvs + mwjh
gshf: qcls * zlcn
zdsv: hnfs * mfrh
cghd: 13
ljtp: 3
qbww: 17
jwsq: 3
jbzz: 6
vlbj: jrpv * vzvc
mpvf: sjcf * gzgg
jlgr: lphp * wvwb
wjvn: 2
vwzq: hdlf + rwlg
mfjz: 7
wmdz: 3
fvtj: dtrh * zlrz
sgng: 2
gcsm: psns - lzpw
jvbh: 3
dtpb: fswr * tbtw
hrmz: 2
rvwf: bscm * cqfb
zmpg: qwrd + twhm
gqjw: 5
pshf: qtbp + tgjf
czhc: lrhn * hcng
tnqj: 3
mpmr: 4
hvvq: 3
vdhz: 3
hghd: 3
dqpc: ngqc / vsnf
zbwf: 3
czlf: 6
blwf: 2
wfsg: zbtd * pzbh
scpn: 2
wfnp: ctww - thbw
nrjf: vwtw + nclp
sfmf: 4
sfqg: tzrj * ndhh
jnhb: svvh - qhnh
fwtj: tjfh * cfmn
rfrm: 3
cmhb: 1
hdlf: 4
gnrv: 2
vjjf: 2
mvpl: 3
tqdq: gldv + vrrt
fgdn: pzhf * hnhq
prdt: dgwp * gjtt
jpjc: 2
njds: vbpn + zlql
rlch: 5
dnqt: mqhc + fzlj
lwtp: 4
lthz: 6
tmhs: 1
vcvc: 6
tqhw: 15
wflv: 2
gmhw: gnln + hbgt
ggjt: 2
hdhg: bvjb + bmrv
wbfl: 1
vzqs: 3
mzwb: mpts + thdf
rhcn: crqz - htsn
jvwl: lhqb / grcv
wczf: 2
wmzg: rsjv / mlpm
clvm: 1
wnlz: 5
shpv: 4
cvbq: 9
fphn: 8
gbnl: tdpq * mcrw
hvdr: 9
ssql: 2
nqrg: 4
wtvd: 2
thwn: 12
mbtd: fnln + fvbc
wffm: 5
ddwn: lmlm * gwnj
dzrr: 1
trtf: qpjs + zgjb
spcv: 3
thdf: pgbm + jhjd
mprq: zfpg + zdmm
qqfc: 3
swcv: 19
qfnq: 2
zfhz: 3
glqz: 6
ffvp: bvfh * mtld
tgpj: gcft - nccr
ljhn: 3
cpgd: 2
nfhr: 18
qpsv: vwbf + njdf
gqmw: wtmj + dmsz
flpl: 2
rchb: 3
szht: jfrw * qvpc
dzwh: 19
gtsc: dljc * zgnz
cvtm: tchm + fhhl
sjtb: svpb + vwlb
blct: 2
fzlw: 8
zpjw: 19
fmqf: 4
dfpv: 2
sdbw: hvhr + pqlw
mpsz: 2
zpcp: 2
vmvr: fszl * hdff
bqpb: fpwv * fhmm
gjjt: qwtb + bjrs
rrnv: wgsh + npvg
fjzw: 2
dcgb: 14
zhbm: znvs * ctsd
jwjv: 2
dgbm: bpsf - qddl
cbgp: sftq / shsn
rdrn: znzg * vpjd
rrnb: 7
dfcs: 3
cggf: gdnq * lwjm
ptft: 4
pfvf: mwls + pghq
lrgd: 8
sqtb: lzft + crsl
gsdp: 3
zfsg: bnbv + cgpn
lqgr: cwff - lwrg
bpgc: sjlf * qfcr
bnbv: 4
dhrf: swpr * bgns
dfvf: nqtz + dsvh
brht: 8
bbsf: 4
zlcn: nrlv + zvzn
cgpv: rdwc + grcf
swzt: 3
ljdm: 2
wwzb: jllz * wlzz
vdqm: 2
wpdc: 4
hqwv: jnpn + wjps
jqwn: sntr * dzcm
szlq: czlc + cpdq
rvqw: mcns * gtfw
cgdr: twld + hrnv
jddc: 5
tljz: 8
cjrv: swwz * cfgv
zmdp: 2
qwqm: wwfg + lmqp
sfdr: 5
rmdf: lccj + jndb
mpwm: 3
ltcj: jmbq * zgvf
cwfh: tltf * hwwm
vccm: 3
vrpt: 2
jjsh: 3
cvgv: 2
sjgh: 2
wbzh: 13
whws: pjqr + dnpw
jljm: 4
qcfz: 2
jjgc: zdbs - nvgh
gvzv: 3
ndgb: 2
bmgt: 2
zzbw: 7
tncs: znsn * wvjs
prsn: 6
zrrg: qvmf * nbmb
gbdf: 4
fzvp: whws * jjsh
jrlj: lfgp + bnjb
czsb: pmcz + rztt
wlpf: frhf + hqfj
pzfw: 2
mstm: 2
rvls: 4
npdb: cctq + nrtj
vhzh: gzhc + nzqd
qwmr: 8
gppg: 5
dzzw: nbwh * rzvn
cssz: mcvg * hhwj
dprb: 2
zwnz: qszj / rrjb
bgwj: 4
zhnc: 3
zltd: nbml * bdss
hmtg: 2
lqjc: 9
jdqv: gwcg * bptf
hpth: jgjf * fqmc
lbrz: pshf * gcsm
zgpz: szqw * zrrq
gdpz: 12
dvzs: 2
tltf: 5
jzms: dpfm + zvbl
pvhm: 7
gzjj: tfwn + brht
hcvc: dfvs + mgbb
rmfh: 2
jtst: 7
rfdz: 2
dljc: 2
rdjb: 2
bcgc: gstj + gbdf
tssc: gstb + tbwt
bwdg: 13
bwbn: nhgc - qhsv
shjb: prrw + bfpp
rdwp: srct * nlfv
bqmz: zcdc + zqnr
smvt: brbw * gqgg
tmth: 5
jjff: 6
scpm: 20
hdjh: swvl + hnrv
hpnl: 1
hldm: 5
ntrv: cbjl + szpr
vdhf: 2
vrcq: ctqn * dvzm
cfzl: tnqj + rqbc
bsnf: 4
wjps: mlfg * fbvz
csqm: bqpb / pssb
cwtt: pznp / grrv
hpdd: 4
wcqr: 2
lwlf: hjwz * dbhq
crsl: 8
cnvg: mrws * cpvf
mgqq: 8
jrwt: rshf + tbnj
hrwf: 3
gqjh: cpgj * rrnb
mmvv: 5
lsfl: 3
qbnf: 4
vnzd: 3
cbdt: 7
wgsw: 2
tccw: sdbd + gqjf
cpvl: vhzh * mpqc
czsr: 3
fzbp: 4
mplm: 3
cvrl: 19
mwjh: clbn + ngdv
srjj: dttf * flqs
hzcg: 3
npqh: 5
vvdq: sfjc * hghd
znzg: 2
jhmw: lqpp - sdzm
jdpg: jhwz + rmhl
jnjv: humn - fftb
wvzj: 8
nqzl: stdr * vfcc
phcg: 5
swvl: gqjh - qctc
cspt: wmdz * wtqm
pdtt: dwmf - zdsv
rlwj: 17
pbmv: vgzv * scfc
hsjl: 19
nzvt: tvng * vmjq
fmqz: 4
wtwh: 5
gfnc: 19
mnbq: vqqg + vnrg
vfgv: zfrs - jzfm
grcv: 2
lgnb: 2
jlwt: gznz * mcfn
rvpt: 5
cnpj: 2
bgcf: cmzb + clgs
whdz: 2
cmmt: 19
jppq: 5
vltr: 3
phlj: tsrb - wltl
vgmd: 3
djft: qlsn + vbql
vpsm: 13
zdvl: 8
sbhf: bpsg + rnsz
zcct: 3
hmhs: 5
lhbn: wmbc * ljdm
cpph: dgbm - cjqm
qmfr: 3
zddp: gnlg / zshc
lpjw: gwdg * bwvh
dlrb: vzhz * pzfw
zwjm: 2
hqfq: 6
qssg: hhnm + mqbf
rqqd: gmpw + qpgp
rlhl: 2
mlfg: prwc * vpmq
zfpg: pwcp + gqms
qjjh: 2
tmpn: bjrh - mvjt
ncss: 5
gsqs: rqld + tlvc
jnrq: 1
dbqf: tfnh * fphn
vpfn: smlf + zhpm
wwft: shlc - dpdv
bqgt: 2
vslm: 3
cpfb: 2
vmjq: 3
rmqp: rwvj + qhqd
jltn: chjg / gcjn
pgnc: hpcw * blhh
pqdn: 3
ffsh: 3
zwfh: nwzw * bshc
vrpj: 2
vggt: mvzb * hlrg
tszg: 5
cwbv: 2
hrwb: 2
rtgh: rdrn + czsr
wllj: 3
pgds: dllm + sdlr
lslb: jvwm * zrrg
qzlr: 3
hvgj: trgt * hlpt
fggh: rdlb * wtcj
vpvg: 4
qghd: 3
ndbl: snpr + sdlh
qtns: zgnc - zqfl
bspb: 2
tdgq: sjgh * pshh
rfmc: gsvq * wwnw
chmn: 2
mvqh: clpg * wlrv
dpss: 2
hhjt: 8
qgfd: 12
mcfn: jrmj + clnt
frqw: 15
zwfj: hpnl + vnvt
dqrw: 5
vjcc: lrhm * qlhm
hqfj: wdhz + lddd
hzng: chsz * hcrc
qjhz: 2
srvm: 3
jqtn: 3
qmnf: jgqw + hjqh
cjwv: bvfq * bcrc
rpcn: zgmm * rlwv
bmtn: sbff * zcsm
jhwd: mwvh * ljhn
hcnr: pnwd * fjfv
ftnv: zdrp * cbtt
znsn: 4
tjns: ljfq * plhd
ldpn: 10
jllz: 3
dpfm: pfvf * jwpm
lqpp: qgcv / jnnc
sjfr: 2
wvjs: 2
cdjg: 4
vhvh: rsvv * mfhp
vsnf: 3
bhgd: tvhp + qcgs
twrw: dbpw + jqwn
czql: wljg * bhrr
bbct: cqtl * bhjq
bpll: hsth + bnwl
pwcp: qdbj * zqld
fzrv: 2
szdh: nwsb + rvmg
fffj: 7
bzzv: 9
qdbb: jqtn + vrcq
wgqt: vgrq - zngb
dlvb: cgcs + gsvv
bwvh: 2
stpb: fpbq + tdlh
psqc: gnhm + rwbv
cnbm: 6
rmcv: nwgn + gvhz
nrtj: zqgt * pths
vpzg: 3
dcdl: dqrc + rjhv
rzzs: 4
mmcp: brqw + wbwd
htmt: qpvs - pzrj
wzgh: mngl * bcgc
sslg: jljq * cgjf
nnqn: njds * zwjm
sdwm: cbqz * lgwf
vrcw: 2
hrvb: tdvq - wqdg
zqcm: 3
fhsg: vmjf * tvnd
rzch: 12
wmnm: 5
gslf: rvzw * jppq
cthn: 2
fcqp: rcvm * tzfg
cqvh: sjls * dcsr
frfv: mntq + rvvz
cmdh: mvqw * lvnl
fszd: 19
hnrv: dbqf / lchg
lrhm: 7
pjvh: bvvd * bdlf
frsm: nqrp + scwc
bqjs: sqtb * rhsq
mvzb: hnvb - ldvm
rgml: 2
chnq: cvsl + nmmg
sgmb: 17
csmz: 5
bstj: 3
zcpn: zwjz / dnqt
jqfq: 3
lhqb: zpnw * nmdh
wlft: pwcm * flwj
srhq: wbnh * wvfh
qlhg: 3
fpdl: dhtj * wbpf
jpvw: vjsb + tqvr
bdsc: 4
zgzv: 1
lbft: bfzh * pbff
mhrv: gbfs * mhhl
hjqh: vsnh + vqfc
qvjt: gcss + drrl
bfwh: 3
gcgp: 4
brvc: 19
srrv: jltn + wsdt
zfcd: 2
smts: 2
fnhd: rmdf / zfmz
jbtm: gbtv * jrhl
qgjs: vqdq * gbnl
ffrr: jdhl + hczp
qpmg: zbwf + fbvg
pmnp: 2
jncz: 18
nhgm: gjvs * cstf
bzzr: vtzb + wrds
dnqp: sfnt + csbb
vgfj: 5
ntzc: ncrs * wdnp
hwwm: 2
flwj: 3
cctq: bhqn * lsrp
nnrg: vpcz * lqgt
hddl: 8
hvlb: hsnh + vwjb
nqrp: 9
rfwl: gsvr / jgdn
rvnw: 2
swlf: 5
cfgv: 2
qqjh: 2
gvhj: sslg * vpzg
qsps: 12
tscn: pmvp * nvht
rhsq: 3
hqzr: jcpw + zwvp
pqfh: 9
sjlf: pnff * dqrw
jfqd: cvtm + csgg
zrwj: fmnb + lbvn
svch: 2
wbvs: tsdw + cmmt
snll: 8
rzjr: 1
twcj: zrpz * msdg
mqwl: 3
znlj: 2
nfzs: bjnf + sngb
wlvn: 2
wwpq: 2
lbzg: bjhm - vslc
vcqs: cptf * wcwd
trql: rtml * jlfz
gfzw: dfqj * vlbr
jbrb: 4
cfrg: zsvb * lvgq
btmj: dshd * snll
pqml: 3
bffs: 20
wnfl: 2
mjnj: 11
bvmd: gqzg + zzhd
qjrr: qhzj * rfpr
qmsf: ldrj + tqqg
pdfq: wldf * fssq
bblj: wwpq * cgmt
svcl: 2
pnmc: stmd * mrpp
jpjp: mfqd + sngh
pgpl: qjgl * pzlm
ptjj: 5
lwcp: 4
gnln: vcvg * dfpv
dbhq: 3
ctll: rtbq * vzcb
qjgm: fsgj + sctd
qmsb: rrds + glrr
hdff: 3
tttd: 15
fplh: fszd + ffmj
lgzp: pjcs * sphj
lmzz: sztj * tvfj
tjcr: cgpv * mlrh
bbdl: 1
hvhr: 2
rgfd: 3
hpcw: chmw / rggw
lwwq: 3
zvmb: jnjv * scpm
qvdr: dqpc + rhmr
pgmp: zcnm * sbgm
lnbb: mhrr * qzbn
bjlr: lcjd * qlnb
cdzf: wlsb * gcds
nnsf: mjrr / wtvd
jbln: 5
dfzj: stcr + cvcf
cmln: 2
mlpw: 2
tvfl: 4
thwh: spcj + bbsf
vvdm: 5
lhtp: wslc * tzjg
dwjl: pvgg - plzs
gplj: dcst * zlgj
jgfq: grgt + dvln
dwfg: hvdr * lzgt
cptr: 4
hmds: 11
pshh: 4
brqw: mfqw + gfnc
pghd: zfhz * pqqm
tnqm: lvtt + mzms
swrs: jqhz * wtsj
hhvc: 2
gnmp: 11
cstf: 2
bhqn: 3
gzsd: nqcd * rpwn
httc: 5
dgss: cdrn * msgg
lrhh: qvjm * nljn
rbbm: cjzv + nhfs
zqwv: ddht + jpbc
lzft: cwst * tpmb
gpbv: vslm * zqcm
snjl: nqgn * qtls
nrhp: bjnd * bwcr
wsjg: 1
gltc: 2
ddcv: 9
dhrt: pjdt + czql
rvmc: 2
mjcq: jgqf + rbhf
ftng: thbj + dvms
tgbj: 3
ztnj: fwvv - wwfd
mcvg: 19
jhjd: 4
rlwv: bmtn + bwwc
wlsb: 3
ztcd: 2
rqtd: 1
jlhb: 4
bzql: 3
nssh: 2
wbgw: rbpd + qgfd
gqqf: vncf + dwjl
dfcf: pbdh * prbd
rdnd: bpgc * qrrw
qgcv: szdh + jmtw
cpsc: 19
shmr: 9
pbjl: 4
pjgp: 9
pths: 5
rvmg: mqvp * trtf
wjfz: fwpt + wwzb
pfhb: rdsf * tsvt
shlc: 10
bjqz: 4
ffzd: 5
wmhq: 11
sfnt: 5
mcrg: 3
qrwj: vhvh - bctb
wvwb: 3
zpcw: 9
zgqn: dfcs * wpzf
bvvd: cgsz + rmmd
wpmp: tljz + tqrh
scvr: ttbs + swrs
sshc: gjjt * gsfz
pzhw: 8
zfmz: 2
gzhc: rwcp + qjhv
mgbb: rhjg * bgcf
tbsl: 3
ncft: cvrw + lbzg
qsdc: pbtg + bwfz
vgnj: 2
wwmb: zwqh + htnf
zzmc: 2
qjgl: vvsl * fjzw
fhpc: bbzq * dqst
jvwc: szgh * tdgq
cvjz: wflv + cspt
flbs: pnmc * frgd
mdwz: mvrs * hdwg
tqqh: hffj * frtb
dbnt: 2
rzvn: 6
tmcn: frjs * jblc
zrcv: ltcj / pcmg
glmq: cszj + wmzg
dbpw: fqbq * qwbz
nbmb: 13
wlzz: 4
gjpw: swrm * nznf
bjht: mzvj + zlsw
nlfv: twwf * vfgv
vcdj: 4
psnf: wwgv * bsfh
pfbp: bdsc + smdr
nfwf: wlfq + mlnt
qgwl: 11
vzhz: fmmm * trbt
zlvn: pfbp * bvtp
cpbh: 5
sqnf: 3
lvwj: 7
pdts: tjcr * vfrr
zlzz: sptr + lszs
pvjr: vhll + wvlc
fwvv: cdzf + vqmw
rjjv: sqdq * tvsg
vgcn: 11
lcgg: zwfh * jwzv
nbmd: mjfz + mfsr
jwzv: gfdd * hscg
mlbn: mrgf * vrmt
mhrr: 4
jvjh: tnzn - zwnz
ftmd: tgnn - mcrg
sptr: 15
cvcn: 2
pftw: drst * hsjl
gcjn: 3
vrjs: bhql + vmgg
tjgd: mtrp * sbmq
hmpj: vjjf + zgwm
vmvg: 2
mlhm: 2
tvrs: 2
rsjs: 14
tvnz: nfzs / zcmq
pvgg: tgbj * cclq
djbf: 5
nsvj: 2
gnlv: qwrn + vjcc
lddd: jcvw * cvlv
wtmj: 14
fmmn: 3
qrfc: 7
grnz: zddt + rfzm
bvlp: njvw * cdzb
pqfc: dmfs * lwwq
zndw: 2
gtvz: frvp + nzvm
tfll: flvm * mzzr
hdhb: mfvq * qrfc
btfb: srws * jgvz
nrdz: wvlj - cpgd
gqzg: 3
srcw: vgqv * tfzr
csmt: szht * pscb
rljl: pmms * dtqg
cpdq: 15
hlmp: ldnh + dhrf
pgvt: 19
wrjp: ntwf * ltmp
jgpm: 3
fjvf: 2
pbrh: 5
bjmw: dlqf + plfm
rtpq: nrcb + dwvf
gwff: 20
zmcq: sfpj * jmqf
tqvr: tnql * cmlq
tgnn: wntt * pdcn
vvsl: pgds / vbhp
dfpm: wnlz * ghgm
jdzb: mdbf * sqpv
hzbf: 12
mpqc: cqnf * sqvt
qpnh: wgwc * fbvh
srzd: 2
zgmm: 2
qwnt: bbpg + vgsm
wngr: 3
hcmq: 1
nmpw: hvgm * wffm
zlbt: qdll * mjnj
mnlp: ppjv * lhvv
zgsg: 2
zzwf: qtjb + mcgs
nlwc: 13
bbvq: 2
rpjh: pftw * jpjp
gmlh: mpfr * lqgr
jwmc: 2
pgsv: rlhl + wmpc
bhvn: 5
djfd: 4
bpsg: 2
fmhh: ffgj * snqn
scmw: 7
bpsr: mhrq * fftm
sqlq: wqld + vnjs
cgpn: jjgc * zjtg
stvh: 1
vtnm: qzlr * tqft
nlth: zpfn * tddq
qtjb: lqmd * dpwg
tmhh: 2
fcsw: zbzs - zqnb
fcvp: 3
wvfh: 9
wvpv: 2
rfdq: njpz * hfdf
vmwr: mdps * tmth
dmhj: sjcl + lrhh
crzs: tqlj * tfll
zcjn: shmr * qffz
jwrs: hnbn + crmh
brhz: wscd * cwgj
mvfw: 14
hqfm: lvhp / fzbp
wqtm: nlmg + gqqf
zcvm: fcnt + njlr
wsnd: 16
pbwm: hdhg * tlmt
ddmj: 3
zwmv: 2
bqmp: ngpw + npqh
dddj: jqfq * wdqm
fstr: wcbp + jvwc
wqsj: fjvf * qbvp
mfhp: 2
hlwb: wbzh * svgt
vwvb: mvvn + mtzm
brbv: dwrd * hncb
hlpt: 2
wzpf: 15
cmlq: 2
lnvw: jwmc * zjss
cnrl: 2
hdtq: pgmp + fqdw
grcf: 2
jlbl: 5
dtcn: qrgb + pzth
fhgp: 19
jcmd: qfwv + psqc
zwvv: 3
bcqh: 2
wrml: 14
scjh: 11
gdnq: 2
gnjp: dtzs + zgnr
rlwf: tdbb + vgms
dthm: 1
lbvn: mrjc * brnc
pbbs: jqds + qrfg
bvtp: 2
vwjb: lsfr * zflg
vbql: ndld * qgnl
fmfh: 14
bqlb: 3
zgpw: 4
gwdg: 5
qffz: 2
pdps: hwcp * zzpb
jhwz: lpsg + gqtn
rtmv: 2
sphj: qtnj * jwjv
vfcc: whjp / fffj
gsvv: 8
vjdv: 9
jmst: dmhj / pqsz
tfgb: qgwl * cvts
qwwl: 2
lgmc: 2
ppjv: 5
lwsw: 4
flqd: gdhz + lhwj
stdr: 3
zzbp: 3
ngjw: 3
snpq: rjzb + bnzl
dndc: 5
fqmc: bhgd + vwvb
rgmz: 3
whhn: gqvl + clvm
btjp: 5
dmqb: 2
qpgp: wvzm * wbcq
hjwz: dwqj * chgz
rslf: 2
zpnw: 2
mhrq: 3
pqtr: 3
rdzq: 9
jnbg: 2
ndfm: ctll / mcnn
zzgf: jlbl * tgnl
qnht: 5
hcng: 3
npjl: 2
cwnp: zhsd + cfrg
svpb: gncq * rtlb
mcrw: 7
drst: jqms + gwvr
lhrd: gltc * bffs
ctqn: 4
jcgp: lvqc * hflp
lgwf: 2
rrdb: 3
rmpt: mhtf + rdwz
fjml: brvc + ldpn
trhd: wngr * hvgj
lqgf: 5
vvbw: hmvr + fshr
bpsf: hcqs * lgwb
jjwm: 2
bcrc: tbjz + phgr
tchp: fvzc + gtsc
rchr: 8
cvcf: gdds * zjsc
grrv: 5
tpml: 3
rfjq: wswt + pqbw
bbfj: 8
wbnh: rcjj * smdv
lsrp: jdnb * bfwh
nnmp: prcd + sfqg
gjbg: 9
tbtw: wzgr + rdjz
bjmh: 2
hrqc: 5
hrrs: 5
cnqc: jlsb * nbtt
ndsj: 2
hltp: hmcr * glnl
wprn: fggh + gfbw
rjsr: dtwc * jvbh
pgsg: pwjp / lgcm
wvlc: mzwb * hpth
rvzz: 5
lfcz: nnhw + gtvz
djcp: ccgr * gvcg
qhrt: 2
bmjc: 14
ngdv: dvvj + ljsh
frvp: bvcw * tzzd
jnpn: zmjz * gvhj
plfm: bjmm * fjhm
wffc: lthz * rfdz
hdmg: 5
pqqb: 3
jmdz: 3
czpw: srzd * fglp
nhgc: vzqs * nshq
fssq: 3
gfsn: wstn + hnpc
jncv: dlvb + ncph
nqgn: 2
frfc: 2
sftz: 5
tvvn: 19
qmsz: hhvc * cvjz
gcdj: wvfm - tcbh
lfgp: 8
jnjm: 14
zrhs: sgmf * qsdc
zqdb: rpzc + drfv
sjpd: jwpl / fbjd
bncf: 2
mdvg: swbl / qwwl
ssjq: 9
qpbw: 4
tjrl: 3
gmpw: vgcn + rlwf
zgsc: gnlv * qtnm
mdpv: pvsr * grlh
rbmc: mgqq * gnsr
wzzj: dfgj + rvpt
bttr: 19
jvwz: wmwr + vrpw
nrlv: 6
sftq: gsqs - rrqq
pqqm: 15
ndsm: sqnz * gzdf
dfzz: 5
wtjp: 2
czlc: gnbc * hdmg
qjdf: 6
jbhg: 2
gbfs: jltr - wnbr
fvlw: nhnb * lvmc
svzb: tzpq + zgzv
wlsc: 5
szgh: zqfq * ghdw
wgvh: 3
qsbq: bwrv + qhlg
lwdr: mhzz * zndw
trgm: 6
zjtg: 2
tpsd: 13
mjfz: dmvw * jhmw
bptf: bqmz - vrjs
cfhs: zfjq * mpjd
hbgt: jnbg * dtmm
hwts: ghnv * qssf
chgz: 2
qsnw: gdvj * zfch
lvvb: 3
fmmm: 6
vmtz: 1
fwpt: 17
mhvf: 5
hwqf: 13
lzpw: 4
dpdv: 3
mfqw: 18
crqz: pswd * mbgs
pwjp: mccn + pwng
qcls: 3
nclp: bbtm * nrcl
vwtw: 9
htph: 2
mvqt: bmjt + bmzs
svmc: rghn + dmcl
vwlb: bzzj + nfjp
cvlv: 5
wtnp: 8
rfcq: qjjr * jttn
wwbh: 3
cgtm: 2
crcq: wprt * czdq
nqfb: 3
bbrw: tcfn + jnrc
rcvm: 2
mcns: 2
rcfs: 5
vdgg: 5
tqvn: 2
jdvj: gcrb + wzhd
wqdg: 3
dshj: vbfp / wrlw
rvbv: 2
pcdt: cdlt * bwwl
sgss: 3
rhqc: gnbb * fqsd
lzdr: ghfv + rprs
dppf: 10
rdsf: 11
ncml: 3
trcc: 3
dsfs: 2
zrpz: 5
wmhp: rrwc * btbp
bwrv: wphf + hdrw
wwms: 3
qzmr: 5
rdwz: qntn * hnhv
djfz: rmsg - tphp
pssb: 2
jpvn: 3
mwvh: 2
qjms: 2
jwpl: 14
rttr: 2
drls: 9
trbt: 2
vgzv: 3
jfbg: 4
vfrr: 3
mhzz: qwmb * lfrt
tlfd: qwbw + hrgc
wnwt: 4
gnpt: 17
dmbb: 5
sqpv: mptl + wqtm
nrjs: gshf - grjs
vwmz: 3
vpmq: 3
wmpc: 4
tvfj: nbmc * lwsl
lmvz: rljl * qtns
tvjz: fpdl + bqjs
jchj: wpgl + lrgd
fhlv: dqng * hrwb
wnvv: 5
hcqs: 12
wcbp: zbln * prff
pdtd: 2
pcdb: 1
bdcj: mhjd * dfvb
pvpf: 7
mrjc: 4
rhqz: 2
gdqw: 3
wgsh: fvlw + dprm
hnfs: 4
trpb: cwbv * zfqs
hmcr: wjgt / zfcn
hflp: 6
bmzz: 1
ptjs: cdtl * jgvd
zsvb: 2
rvmz: dzsg * vgfj
ljwj: trgm * qqfc
nljn: 5
zqhd: 9
vmvc: 3
pfzw: 2
tsvt: 2
zrww: 4
pwcm: trlz * frsm
jfrw: 2
dljp: tzhz * cgtm
lwgs: 2
fdfb: 2
wvzm: qbvl - trpb
lmlm: 2
dsrm: cgqm + sfnf
jrpc: dqqh * grvh
fsgh: pjfz - dvqf
stbf: rttr * bhvn
lzdt: 4
flrn: djpb * lllb
bjfc: 3
tvdb: ftnv + bmzz
lvrr: bccm * rwzb
ntjm: nbhr + lphl
wlvd: ncml * qvrh
htnf: sgfw * gmlh
sfgv: hqzr * pjsq
lvpt: 3
jrrw: 2
mdtn: 5
zvrt: gmhw + fzvp
wsff: 16
ngnl: czlf + lsjr
wrlw: 2
wwgv: 14
sbzj: hdbl * qbfg
wrff: 2
lwbt: 4
hczp: 3
grlh: 10
mvpv: 4
bgnt: 7
wntl: ndsr + dqcv
zltf: pphj * pcfw
rggw: 2
jzws: zrwj * wbvs
vjwj: 9
qzns: 3
dpwg: 3
mhnd: 2
qbbl: dwjr * zvnz
cvts: 2
snpr: 1
vcrg: jpvn + wdng
rjzb: 12
pdzn: jwps * tvvn
sdsm: 17
lpsg: 5
vvhp: qqjh * lwcp
ldgm: zqwv * lbmr
jnrc: 3
rtml: 4
hdgh: 2
rlqf: dwvh + lvtw
vffg: 4
ptgh: bbct + sjtb
nmtl: 2
sqhj: bfmj * lqjq
mfqd: wzpp * gqfn
zsrn: 9
jbtq: gjbn / jtct
mpjd: hdqh + jmlv
qbvp: 5
mjrr: qzjb + cppm
qpsc: 13
dgjw: lmwg + wrml
bvzb: 3
gjzw: 4
hdqh: dvzs + jbzz
jnzf: rldh / wrff
qdvs: 2
fvzc: 1
dhmn: bzzv * lwsv
cblm: nfwf + dvlc
sbff: 6
cjvm: 3
twld: 7
tmsg: 2
gzsl: tmcn + rjjv
rsjv: zjvq * wwld
lgcm: 4
dzvn: fgqs + mgwt
ctrs: 2
mzzr: zsmt + vffg
bwwl: 3
hmvr: 5
nnhw: wvdr + wrjp
rfpr: 3
vbpn: 3
ngdm: 3
vfsc: 3
mlrh: 3
pjcs: qchm * zrbm
jcpj: 4
lvgq: cjvm * bfjr
qrrw: 10
wflp: fbvn / nqfb
tgrc: lgzp / dmqb
jgjf: 2
vslz: nvnb - qgdf
vhmn: zzgf + czhc
brwd: 4
hqlj: svzt * tfvr
zcrf: pbzc + hvfh
jvlp: 2
wnff: 3
cpvf: hcnr / jbhg
ldrj: 10
cwst: 7
ssdj: dflc * mrrd
pzbh: 6
bpfw: 6
jnjw: 13
dmsz: zpvn * wgsw
qnpb: lvpt * rzch
bctb: dhrt + qbbl
cqsc: jtdm + fdvj
grmm: 2
dmfs: dfzj * vsbl
hfqs: 8
hwqd: gcnf + dwlm
zjsh: 5
zllr: wzgh * bphf
vrqw: 2
dsww: 4
ttzb: bjfc * gnpt
hprv: vmqd + lvrr
bfmj: jdvj + rhdd
bgpb: 5
hdmn: 9
prff: ztnj - dlbq
gnbb: 3
ggcg: jrlj + tmhs
cfqs: ljwh * hlwb
rdml: slnr - hdjh
vdgf: 2
nhfs: 14
nbmc: bvnc - dcgb
zgwm: hbst + zpjw
jgvz: 7
lqsj: lszf + bjqz
wcwd: dzwh * zzmc
tbjz: zlnl * cdjg
pwpp: 16
sgmf: 2
fmlg: pfrh + ppnz
wgrl: cnlt + ztfq
ldvm: 3
mtqf: 9
hbvw: vvbw * csmz
bphf: 2
vtjr: 3
qwdg: ngnl * cpfb
cccl: 3
pjfz: srrv / wgzq
cfrd: 1
jbll: mvpv * vlsn
vqfc: 2
rdbb: 5
rwlg: 3
trgp: wsff + ztrv
rprs: sbzj + jgzd
jdnt: 10
vcvg: szlq + srnw
hplr: bdcj - vspg
sttt: 2
zngs: pfzw * zgqn
wdnp: hdgh * zqhd
lvtt: dzrn + wdzv
sctd: bpmv - fgqp
fwfr: gbzg / vrpj
vnmq: 14
bfzh: 6
fqst: 2
vcgl: 2
qbnm: 2
rqjz: 7
sghw: thvg * gvqz
qgdf: pbwf + rczc
tljs: 2
sjtj: 13
jvwm: nrjf * tqwf
twgm: 1
bdjt: 5
zvjf: 4
vcgd: 7
qrmr: bzzr * bstj
bwwc: 1
ltgr: 3
dcbf: cqsc + cjnt
mqbf: 5
mbgf: 4
zvzn: vgcl + vwqs
gvrh: 7
vgrq: wtjp * lhsv
bwcr: 5
bwfz: 12
bwdp: 3
blcb: lqsj * zzzt
gfsp: wrnj * nnsf
cgzb: ftlq * lwgs
jhcz: 3
nnvs: ltsj * ptff
sfpc: 2
qbwm: 5
fccc: 1
wlrv: mpwm * wgvh
nlqc: mbtg + zfsb
tphp: 5
ppml: 5
dpsf: 13
htzt: 2
gzch: pdbf / dmgm
pdcn: 5
czgl: 2
lmdz: 2
cpwr: 3
rldh: gqgp * qjpj
svqp: rmqp + zlnd
tzlw: jlhn - mhrv
sccr: 2
mjpd: jdnt * hzcg
jwps: 5
bcrr: hwqd * sjfr
tbgp: 3
rrjb: 2
djpb: tzdn + wwdw
clnt: 5
pjsq: 3
lbmr: gnmp + tljs
zmrz: vzdz * jvdp
bhqc: 2
dcjd: 3
bjrs: 7
rdtg: tvfl * qwdg
hltr: 5
mgwt: 5
cppm: mvqh - wjvn
vbns: jbll / lwtp
mzms: bmjc + svmc
rmhl: 3
tzfg: wtzt * jzsh
lzrp: 13
ptrm: nvdj * qpnj
hdwg: 4
lvsf: smvt + qjsf
wpgl: 11
zlzt: jljm + hfls
pwnz: ndzf / mfpf
dlzw: 2
dtmm: lbft / ntjm
bsmc: 3
btbp: rbdm + rjpq
svzt: 2
hcrc: 17
hdtf: qrmr * lsfl
shff: hdfl * qhsd
dmcb: 7
qvmr: stvh + bwnn
fmzs: 2
gcss: 4
lqgt: 2
srjm: ntzc + zfzv
lzcr: 4
wlfq: bwdp * svlp
nwvr: 4
pcgv: pdzn - thdr
mhbj: vrzg / tlbd
zlnd: vcrg * wnml
rzzl: 2
pphj: 3
nfjp: 19
tbhm: 8
svlp: ffvp + srjf
hsth: wtnp + qcjb
zgvf: swrv * bqgt
qtcg: 5
bvjb: 5
frhf: wmhq + hzbf
vgfw: 1
nphz: ggct * wmlp
zdwz: 4
mqhj: prsn + qcjj
hwfh: brbv - ndzr
glrr: cvbq * gpbv
thbj: 2
cqwc: sfsg + lwdr
zdrp: 7
zhpm: tsfb + mlgb
nhch: zfsc + jlng
gsvq: cmdh / dlmd
gjvs: nnhg - lbvb
glfd: qzlh * zlzt
zrml: 3
sqcz: jrss + tbpq
bdss: nclt * rsnd
lbfz: vqzw * shpv
bzdn: qqfj * cwnp
hqvp: tgpj * fmmn
frqt: hcvg + rtjq
lgqd: wbzv + rfjq
zpqj: twnp * lbfz
wcbw: qmsf * vwht
dmcl: ffzd + rchr
rczc: bgbj + djft
qwrn: vvmp / svch
jqhz: 5
wprt: 4
vslc: 2
tzjg: szjb + nlth
wvrj: 8
fgff: 3
tdlh: 7
vpjd: dfpm + pdnz
zjpc: qfvh * nhpf
qfwv: dhmn * bdwp
nbwh: pvjr / npjl
fhmm: zwzc + jqmg
tbpq: zhvh + mjcq
hcqh: 3
mzgc: wnwt * wvrj
tfvr: zvrt + pmbz
sfpj: wlft + fmlg
crmh: 4
crcw: mslt - cjwv
bpfn: tjgd * cqrw
dcsr: 2
ncrs: 8
wtqm: 5
tddw: mvqt * vdhf
rrds: dljs + srcw
hsnh: rpjh + rfcq
lnbj: 3
vqzw: 5
sdzt: ddmj * sgwv
ndsr: rchw - qvnn
rwbv: hmpj + dzrr
ztbn: gnjp / cvjw
ctww: 8
zcsm: 2
tctb: pcdt - zhnc
bsbf: 4
lwdt: fdmq * rpdt
rfrj: 5
tfzr: 3
wvdr: hddl + dmbb
sfds: tntz + qgpl
llmm: bqmp + qsvt
jzsh: dfzz + rsjs
hpwq: 12
bdds: gcdj / hdwh
fwgn: wffc * zsvv
rwzb: 2
qzqs: 4
pbff: zntn + rdbb
qdbj: 4
wjrf: tnjc + pgpl
zlmh: 2
grgg: 3
nftj: bbnv * dfbt
wjnq: 2
bjtn: 3
rrwn: 10
wrbm: 2
gnhm: 2
mbqq: jtvf * nmtl
zzhd: 14
vnvt: wtwt * hdbw
nwll: 13
sdlr: fdrn * mfpn
hnhv: 2
dfnf: 3
tlbd: 2
rsnd: mpmr * smts
fvrv: 4
dlmm: 3
znvs: 4
crqs: vlfp / hltr
dpgm: 3
gvnt: vzpn * pvhm
qqvm: bvmd + czpw
bqgd: 4
sbwg: 11
pglg: hlvv * dvcc
gggt: 6
csbb: 18
zcmq: rqtd + znvp
zdbs: 12
lqlw: zgsc / lvvb
shsn: 4
qcbf: gvtg - ltjc
hznv: brwd * gcgp
vvdw: 11
wvlj: gjdb + fhlv
pglr: grqd / cthn
htsn: rfwl * dcjd
sngb: zsdm * jfqs
smfh: 3
mfpn: 2
vnjs: 1
gjtt: lggn * hvlb
bqvq: 3
mrfm: hrwv * lvgh
vmgg: bttr * mwsv
hspg: 2
nvnb: pwvw * nbmd
hwcp: 12
tbcm: bprd + rdtg
rpwn: 3
tfwn: 1
qsvt: 10
pqqj: 3
zlsw: cvhl + brms
wcwp: cfhs / pmnp
fbvn: jlgr * rtgh
wdhz: vdqf * qtcg
stmd: 2
ptsn: 2
cjgv: 4
zfjq: 2
zzzt: cpvl - vcqs
wscd: hdtf + lbdb
frlq: zfsg + gcnd
mptl: pgsv * rvzz
vwbf: mzzp * zdqn
jzhb: cwmq * tfpj
tfnp: rhqc + pqvw
sbbv: 12
vncf: 5
lbzv: 3
qwmb: szzz + wrbm
bltf: 7
qstl: qdbb * rlrz
srpq: 3
ccgr: 2
fbvh: 8
srjf: 8
psns: zclh + mzvr
cclq: ljwj + ncss
hdbl: 3
vrls: 2
szqw: 2
jlhn: gfzw * jrcc
wwnw: 2
vqfm: zsfq * qwqm
ltmp: 2
qqfj: 2
glnl: 4
bvcw: 3
njvw: qhjh + cvgv
bhjq: vlvf + hmds
thdr: tmhh * qzqs
rtcr: 3
rpzc: tvdb * gvnt
zpbs: rtvd * twfz
ptff: 3
fqbm: 7
gqtn: grld * dprb
fglp: mbtd * ncvd
wmzm: 4
qdlb: 3
nqsg: zjpz + shff
bqgc: mqrr + gsdp
mhjd: 3
lqvq: 1
gstb: 12
cdpl: nbqp + hwts
tpzv: 2
nsdm: shqb * rchb
hclz: sdsm + pghd
mtgp: 8
wjpw: mstm * hqvp
gmwl: 1
tzzd: ptft * pqdv
zpjf: vgnb * tjrl
ntcm: 19
tgjf: 3
rpdt: 13
dnpw: pmlt + mmlq
hgmz: qvdr - lgqd
trch: dtcn - flrn
hhnm: 2
ppnz: 1
qtch: 4
pjbq: fzns + ghtt
rzgh: pmvs * wcwp
wpgt: jnjw + nqrg
lwjm: bhmg - bqlb
wtwt: 16
dzdm: pjlj + jvjh
spcj: 3
ssqq: spfm * wjnq
tzdn: 5
cjqm: bfgf * smfh
zclh: bdjt + zgsg
srnw: jwjf * scmw
dshd: 3
nbqp: 1
vmqd: bjpg - pcqb
bbpg: wnff * wqnj
jbsn: lwlf / ptrm
fpbq: 14
zsjp: 4
hnhq: 2
zlgj: 3
gsfz: 2
ndbj: 2
vlvf: mszw * mmvv
rtzw: mwzp - bbrw
sjcl: sttt * psdd
jjrp: qwnt * qjms
mdbf: clhn + csqm
znvp: 6
qpvn: wjpw / djfg
vrpr: dlmm * swcv
lvqc: 3
sjcf: 2
tdpq: 3
zffb: 18
wrmp: 2
tnzn: bjlq * zztp
bjlc: 3
gmdl: zggj * qvjt
vdln: wgqt * rvcm
hlrt: 4
vdmj: jzhb / rvmc
hrwv: 3
nzvm: 10
dnsq: trct + cbdt
wcgs: glqn * qnqf
tvng: lqlw + jlzv
ttbs: ggjt + vmgj
sqvt: 17
scfc: 4
fqwq: 10
jwjf: ssjq - vtlh
jrhl: htdt + zdwz
zntn: jbsn * chmn
bnjb: 4
whcd: 2
rdjz: hcmq + pbmv
dflc: 2
qssf: 2
mpfr: qpbw * whcd
jqds: 17
tlvc: fstr * tnnl
ntwf: 12
cjnt: jvwl * smqd
ngqc: zhfn * bvdf
lflg: ndgb * lfjd
svvh: smjc * fvrv
lwsl: 13
wtcj: 5
rplq: 4
dqcv: mftl * frng
vhll: qgtm * lhcc
twwf: wcjw / rwwz
dvqf: rvsn * rmcv
vlhs: 10
jnnc: 4
tsdw: 4
sfsg: lwdt + vmmj
ghdw: 4
mlzv: qtch * czhr
jmlv: ztgv * qpsc
bgns: slwc + hvvq
smlf: vvcp * hrwf
fgjg: 17
gcjr: hqzd * blbj
wldf: 2
wwvw: 10
qzjq: zqvs * nmwz
hdfl: 5
hdbw: 2
dwmr: jrwt + bvlz
bscm: 9
lfjd: 17
ltvs: pbrh * wprn
jvdp: 3
ldst: tcfm + hhjt
vmgj: jfjl + vnbg
cnlt: 6
vgqv: 2
pvzz: 2
jrpv: 10
pqsq: 2
qwbw: 9
jbmh: mdmw + jwdr
mccp: 7
scng: 6
mzzp: 5
pcch: 2
mstq: gdgl + mbdv
vtdv: cwrs * ggrl
sjnp: hbbr * zjpc
zfcn: 2
tfwq: hznv * pbwm
rmvd: 2
lmwg: zlvt + nhch
gstj: 15
njlr: ppnc * gjzw
zflg: 11
qjhn: cjrv / hrmz
scwc: qdjj + bjlr
lfrt: 2
fncw: jjff + sbhf
lbqr: 6
rthh: 2
tqft: 5
dfgs: chdc + dthm
dslw: 14
pqlw: 5
hzlp: 3
jljb: 3
qhbr: cpgn + fqjn
ddbg: dgjw + qnpb
wsrl: 10
vndj: 2
zjpz: 16
zwvp: 5
zggj: qmvc + przl
mrnv: qnht + jhpz
rlrz: 2
tbwt: srzj + qvgw
qhjh: 8
frtb: 3
rsvv: hdpw + gzsd
whjp: trgp * sdbw
gwqp: 2
gjfd: 11
jlsb: 2
cgmt: bccg * lhbn
rlqv: jcpj * zstg
rfhv: 5
zqld: 2
hrgc: wcqr * ntcm
vjtv: 10
pjlj: lmvz + zsgq
ddjz: bvlp - nhgb
dfvs: vbns * fwrq
nmdh: hlqt + gmhv
qlsn: nfqs + zrbb
rztt: rlwj * mlpq
gncq: dclr + gjdc
hmcn: qbrd * blrc
bmjt: 8
thvw: 20
rcdr: 3
mvws: 4
glqn: jrrw + hgbc
wzgr: jrhz * dppf
dtwc: 5
sgdt: lwsw * zffb
cqrw: 2
frht: 4
nqcd: wcqc + wswj
vrzt: crcw - qggh
cgcz: 8
nmwz: 6
trgt: zrmz + lpjw
qbjb: bpwr * vrqw
zbzs: scjh * gqjw
gfdd: 4
rtjq: cpbh * hmsw
jlzv: bgsc + twpq
lhlr: 3
msdg: 3
vcvr: 3
dlqf: fcsb + szgz
vnrg: lmzz + blcb
vzpd: vggt + vvdq
ctwv: 3
jfqs: vcdh / cmln
npvg: wflp / mtgp
tzrj: 2
gcft: 8
gnlg: wjrf * lwwg
mbtg: mfjz * dfnf
swrv: nnvs + gvdc
wbpf: 4
bsfh: 2
fmnb: 1
jwpm: 2
wbcq: 2
vspg: vlhs - jzmj
hqpz: 3
rdwc: 5
ssdm: wqsj * httc
qrdb: hcqh * vnpt
bgnm: qvcv * zqmj
vmzt: 4
bjzw: 2
wqnj: 7
dvcc: 3
qzps: 2
jrss: pvjl * lqjc
fcvc: 4
thjc: vgnj * cdpl
hscg: 2
tztt: 5
nfsn: 2
gqjf: 6
flqs: 2
gjdb: rfrj * grnz
jjgs: wsrl * bpfw
qhsd: 5
nlbh: 5
tbnw: jngv * cfgb
zstg: hzng - mlwf
vtbw: fcbv * jcdj
jdgg: jptq * sfmf
nbtt: ddbg - lgmh
ffmj: 12
vqdq: rwgg * dnsq
zrlr: 4
rdjm: vmtz + vmvr
ltwg: 2
bhql: lmvh * pqcf
vlsn: ptfc + gssd
lphp: 8
pcqb: qjhz * ttgg
swrm: 7
gwnj: chmg + mdpv
ppqq: 4
hlwd: 9
zclj: bbrp * scpn
nbcn: jbtm + zpcw
vjbq: 4
spfm: 3
wlrg: 5
pwvw: 2
bbzq: 3
jdhl: gbmw * wmnm
jzmj: 3
hfcs: 3
sztj: nwll * dbnt
ztfq: 1
qvnn: 17
htpv: 4
fszl: 2
rmsg: rzgh / vtwn
tcbh: rcdr * fjdj
lhwj: 5
pdpv: lvsf + qjhn
qfdp: wscg - vpvg
rpzb: hlmp + zmpg
vgnn: vslz / hqpz
sfjc: ljtp * jhcz
vwvp: 3
qgnl: hqfq + gmwl
dprm: rqqd + chnq
plpt: rzzl * tnqm
zvbl: cpsc * pqqj
wwld: wlpf / mlpw
rwwz: 3
gwvd: 4
hdwh: 5
hwcm: hlwd + dfvf
vjsb: gpcd + wbbd
zjvq: qjnf + nqzl
vjtq: 2
mccn: vjcb * zhdp
smmd: rtzw * vrfm
mvvn: cszb + pdpv
rchw: pqsq * htfv
bgbj: tfnp + jdpg
fnws: jrpc * hhrw
szzz: jmdz * snpq
hsml: 3
fsss: hhgl + nrdz
szjb: nrhp + rvmz
gldn: bjlc * djbf
wqld: gdqw * fdrj
gcrb: cwfh * hprv
dwqj: qlfp + cmhb
shqb: 5
wmwr: 1
tdnh: jnjm / ntcl
dvlc: nsdm * mmpp
wgwc: 2
rztp: wwms + rplq
csdm: 18
swsw: 3
nwgn: sfpc * trcc
czrg: 9
fgqp: bjtn + gjcv
trlw: nrww + lhrd
rrrz: jcmd + vgnd
tngd: qwmr + hgrp
rbhf: bmvs + stbf
zgjb: mzgc + vqfm
swbl: tqvn * qmsb
rrwc: 2
mgcq: 5
zjss: pcdb + bglm
zngb: cnrl + qpzq
cnpt: 3
"""

from abc import ABC, abstractmethod
import sys


# I copied some of these classes over from 2021 day24sym.py
class Expression(ABC):
    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def iszero(self) -> bool:
        pass

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


class Input(Expression):
    def __init__(self, idx):
        self.idx = idx

    def simplify(self) -> Expression:
        return self

    def __repr__(self):
        return f'IN[{self.idx}]'

    def iszero(self):
        return False
    
    

class Literal(Expression):
    def __init__(self, val):
        self.val = val
    
    def simplify(self) -> Expression:
        return self

    def __repr__(self):
        return f'{self.val}'

    def iszero(self):
        return self.val == 0


class Sum(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.iszero():
            return right
        if right.iszero():
            return left
        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val + right.val)
        if isinstance(left, Sum) and isinstance(right, Literal):
            if isinstance(left.right, Literal):
                return Sum(left.left, Literal(left.right.val + right.val))
            if isinstance(left.left, Literal):
                return Sum(Literal(left.left.val + right.val), left.right)
        return Sum(left, right)

    def __repr__(self):
        if isinstance(self.right, Literal) and self.right.val < 0:
            return f'({self.left} - {abs(self.right.val)})' 
        return f'({self.left} + {self.right})'

    def iszero(self):
        return self.left.iszero() and self.right.iszero()


class Product(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.iszero() or right.iszero():
            return Literal(0)
        elif isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val * right.val)
        elif isinstance(left, Literal) and left.val == 1:
            return right
        elif isinstance(right, Literal) and right.val == 1:
            return left
        if isinstance(right, Literal) and isinstance(left, Quotient):
            if left.right == right:
                return left.left
        return Product(left, right)
        

    def __repr__(self):
        return f'({self.left} * {self.right})'

    def iszero(self):
        return self.left.iszero() or self.right.iszero()


class Eq(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()

        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(1) if left.val == right.val else Literal(0)
        if left.iszero() and right.iszero():
            return Literal(1)
        return Eq(left, right)
        
    def __repr__(self):
        return f'({self.left} == {self.right})'

    def iszero(self):
        simplified = self.simplify()
        if simplified != self:
            return simplified.iszero()
        return False


class Quotient(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @cache
    def simplify(self) -> Expression:
        left = self.left.simplify()
        right = self.right.simplify()
        
        if isinstance(left, Literal) and isinstance(right, Literal):
            return Literal(left.val // right.val)

        if left.iszero():
            return Literal(0)

        if isinstance(right, Literal) and right.val == 1:
            return left

        if isinstance(left, Product):
            if left.left == right:
                return left.right
            elif left.right == right:
                return left.left
        if isinstance(self.left, Sum):
            return Sum(Quotient(self.left.left, self.right).simplify(), Quotient(self.left.right, self.right).simplify()).simplify()
        return Quotient(left, right)

    def __repr__(self):
        return f'({self.left} / {self.right})'

    def iszero(self):
        simplified = self.simplify()
        if simplified != self:
            return simplified.iszero()
        return False


def parse_line(l):
    tokens = l.split(' ')
    monkey = tokens[0].strip(':')
    return monkey, tokens[1:]


def get_value(monkey, dependencies, nums):
    if monkey in nums:
        return nums[monkey]
    l, op, r = dependencies[monkey]
    left = get_value(l, dependencies, nums)
    right = get_value(r, dependencies, nums)
    nums[l] = left
    nums[r] = right
    val = 0
    if op == '*':
        val = left * right
    elif op == '+':
        val = left + right
    elif op == '/':
        val = left / right
    elif op == '-':
        val = left - right
    nums[monkey] = val
    return val


def solve_root_equation(val, eqn):
    while not isinstance(eqn, Input):
        if isinstance(eqn, Product):
            if isinstance(eqn.left, Literal):
                val //= eqn.left.val
                eqn = eqn.right
            else:
                val //= eqn.right.val
                eqn = eqn.left
        elif isinstance(eqn, Quotient):
            if isinstance(eqn.left, Literal):
                val = eqn.left.val / val
                eqn = eqn.right
            else:
                val *= eqn.right.val
                eqn = eqn.left
        elif isinstance(eqn, Sum):
            if isinstance(eqn.left, Literal):
                val -= eqn.left.val
                eqn = eqn.right
            else:
                val -= eqn.right.val
                eqn = eqn.left
    return val


def get_valueb(monkey, dependencies, nums):
    if monkey in nums:
        return nums[monkey]
    l, op, r = dependencies[monkey]
    left = get_valueb(l, dependencies, nums).simplify()
    right = get_valueb(r, dependencies, nums).simplify()
    nums[l] = left
    nums[r] = right
    if monkey == 'root':
        if isinstance(left, Literal):
            return solve_root_equation(left.val, right)
        else:
            return solve_root_equation(right.val, left)
    val = None
    if op == '*':
        val = Product(left, right)
    elif op == '+':
        val = Sum(left, right)
    elif op == '/':
        val = Quotient(left, right)
    elif op == '-':
        val = Sum(left, Product(Literal(-1), right))
    val = val.simplify()
    nums[monkey] = val
    return val


def solvea(inp):
    inp = inp.strip().split('\n')
    lines = list(map(parse_line, inp))
    dependencies = dict()
    nums = dict()
    for monkey, rest in lines:
        if len(rest) == 1:
            nums[monkey] = int(rest[0])
            continue
        dependencies[monkey] = rest
    
    ans = get_value('root', dependencies, nums)
    return ans 


def solveb(inp):
    inp = inp.strip().split('\n')
    lines = list(map(parse_line, inp))
    dependencies = dict()
    nums = dict()
    for monkey, rest in lines:
        if monkey == 'humn':
            nums[monkey] = Input(0)
            continue
        if len(rest) == 1:
            nums[monkey] = Literal(int(rest[0]))
            continue
        dependencies[monkey] = rest
    
    ans = get_valueb('root', dependencies, nums)
    return ans 


if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solveb(example)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual)
    print(f'actual:\n {actual_ans}')

