# -*- coding: utf-8 -*-
#
#    Copyright © 2019 Simon Forman
#
#    This file is part of Thun
#
#    Thun is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Thun is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Thun.  If not see <http://www.gnu.org/licenses/>.
#
'''
Utility module to help with setting up the initial contents of the
JOY_HOME directory.

These contents are kept in this Python module as a base64-encoded zip
file, so you can just do, e.g.:

    import init_joy_home
    init_joy_home.initialize(JOY_HOME)

'''
import base64, os, StringIO, zipfile


def initialize(joy_home):
    Z.extractall(joy_home)


def create_data(from_dir='./default_joy_home'):
    f = StringIO.StringIO()
    z = zipfile.ZipFile(f, mode='w')
    for fn in os.listdir(from_dir):
        from_fn = os.path.join(from_dir, fn)
        z.write(from_fn, fn)
    z.close()
    return base64.encodestring(f.getvalue())


Z = zipfile.ZipFile(StringIO.StringIO(base64.decodestring('''\
UEsDBBQAAAAAAORmeE794BlRfgMAAH4DAAAPAAAAZGVmaW5pdGlvbnMudHh0c2VlX3N0YWNrID09
IGdvb2Rfdmlld2VyX2xvY2F0aW9uIG9wZW5fc3RhY2sNCnNlZV9yZXNvdXJjZXMgPT0gbGlzdF9y
ZXNvdXJjZXMgZ29vZF92aWV3ZXJfbG9jYXRpb24gb3Blbl92aWV3ZXINCm9wZW5fcmVzb3VyY2Vf
YXRfZ29vZF9sb2NhdGlvbiA9PSBnb29kX3ZpZXdlcl9sb2NhdGlvbiBvcGVuX3Jlc291cmNlDQpz
ZWVfbG9nID09ICJsb2cudHh0IiBvcGVuX3Jlc291cmNlX2F0X2dvb2RfbG9jYXRpb24NCnNlZV9k
ZWZpbml0aW9ucyA9PSAiZGVmaW5pdGlvbnMudHh0IiBvcGVuX3Jlc291cmNlX2F0X2dvb2RfbG9j
YXRpb24NCnJvdW5kX3RvX2NlbnRzID09IDEwMCAqICsrIGZsb29yIDEwMCAvDQpyZXNldF9sb2cg
PT0gImRlbCBsb2cubGluZXNbMTpdIDsgbG9nLmF0X2xpbmUgPSAwIiBldmFsdWF0ZQ0Kc2VlX21l
bnUgPT0gIm1lbnUudHh0IiBnb29kX3ZpZXdlcl9sb2NhdGlvbiBvcGVuX3Jlc291cmNlDQoNCiMg
T3JkZXJlZCBCaW5hcnkgVHJlZSBkYXRhc3RydWN0dXJlIGZ1bmN0aW9ucy4NCkJUcmVlLW5ldyA9
PSBzd2FwIFtbXSBbXV0gY29ucyBjb25zDQogX0JUcmVlLVAgPT0gb3ZlciBbcG9wb3AgcG9wb3Ag
Zmlyc3RdIG51bGxhcnkNCiBfQlRyZWUtVD4gPT0gW2NvbnMgY29ucyBkaXBkZF0gY29ucyBjb25z
IGNvbnMgaW5mcmENCiBfQlRyZWUtVDwgPT0gW2NvbnMgY29ucyBkaXBkXSBjb25zIGNvbnMgY29u
cyBpbmZyYQ0KIF9CVHJlZS1FID09IHBvcCBzd2FwIHJvbGw8IHJlc3QgcmVzdCBjb25zIGNvbnMN
CiBfQlRyZWUtcmVjdXIgPT0gX0JUcmVlLVAgW19CVHJlZS1UPl0gW19CVHJlZS1FXSBbX0JUcmVl
LVQ8XSBjbXANCkJUcmVlLWFkZCA9PSBbcG9wb3Agbm90XSBbW3BvcF0gZGlwZCBCVHJlZS1uZXdd
IFtdIFtfQlRyZWUtcmVjdXJdIGdlbnJlYw0KUEsDBBQAAAAAACFrpk7/HHjxGBYAABgWAAAKAAAA
bGlicmFyeS5weScnJw0KVGhpcyBmaWxlIGlzIGV4ZWNmaWxlKCknZCB3aXRoIGEgbmFtZXNwYWNl
IGNvbnRhaW5pbmc6DQoNCiAgRCAtIHRoZSBKb3kgZGljdGlvbmFyeQ0KICBkIC0gdGhlIERpc3Bs
YXkgb2JqZWN0DQogIHB0IC0gdGhlIFBlcnNpc3RUYXNrIG9iamVjdA0KICBsb2cgLSB0aGUgbG9n
LnR4dCB2aWV3ZXINCiAgbG9vcCAtIHRoZSBUaGVMb29wIG1haW4gbG9vcCBvYmplY3QNCiAgc3Rh
Y2tfaG9sZGVyIC0gdGhlIFB5dGhvbiBsaXN0IG9iamVjdCB0aGF0IGhvbGRzIHRoZSBKb3kgc3Rh
Y2sgdHVwbGUNCiAgd29ybGQgLSB0aGUgSm95IGVudmlyb25tZW50DQoNCicnJw0KZnJvbSBqb3ku
bGlicmFyeSBpbXBvcnQgKA0KICAgIERlZmluaXRpb25XcmFwcGVyLA0KICAgIEZ1bmN0aW9uV3Jh
cHBlciwNCiAgICBTaW1wbGVGdW5jdGlvbldyYXBwZXIsDQogICAgKQ0KZnJvbSBqb3kudXRpbHMu
c3RhY2sgaW1wb3J0IGxpc3RfdG9fc3RhY2ssIGNvbmNhdA0KZnJvbSBqb3kudnVpIGltcG9ydCBj
b3JlLCB0ZXh0X3ZpZXdlciwgc3RhY2tfdmlld2VyDQoNCg0KZGVmIGluc3RhbGwoY29tbWFuZCk6
IERbY29tbWFuZC5uYW1lXSA9IGNvbW1hbmQNCg0KDQpAaW5zdGFsbA0KQFNpbXBsZUZ1bmN0aW9u
V3JhcHBlcg0KZGVmIGxpc3RfcmVzb3VyY2VzKHN0YWNrKToNCiAgICAnJycNCiAgICBQdXQgYSBz
dHJpbmcgb24gdGhlIHN0YWNrIHdpdGggdGhlIG5hbWVzIG9mIGFsbCB0aGUga25vd24gcmVzb3Vy
Y2VzDQogICAgb25lLXBlci1saW5lLg0KICAgICcnJw0KICAgIHJldHVybiAnXG4nLmpvaW4ocHQu
c2NhbigpKSwgc3RhY2sNCg0KDQpAaW5zdGFsbA0KQFNpbXBsZUZ1bmN0aW9uV3JhcHBlcg0KZGVm
IG9wZW5fc3RhY2soc3RhY2spOg0KICAgICcnJw0KICAgIEdpdmVuIGEgY29vcmRpbmF0ZSBwYWly
IFt4IHldIChpbiBwaXhlbHMpIG9wZW4gYSBTdGFja1ZpZXdlciB0aGVyZS4NCiAgICAnJycNCiAg
ICAoeCwgKHksIF8pKSwgc3RhY2sgPSBzdGFjaw0KICAgIFYgPSBkLm9wZW5fdmlld2VyKHgsIHks
IHN0YWNrX3ZpZXdlci5TdGFja1ZpZXdlcikNCiAgICBWLmRyYXcoKQ0KICAgIHJldHVybiBzdGFj
aw0KDQoNCkBpbnN0YWxsDQpAU2ltcGxlRnVuY3Rpb25XcmFwcGVyDQpkZWYgb3Blbl9yZXNvdXJj
ZShzdGFjayk6DQogICAgJycnDQogICAgR2l2ZW4gYSBjb29yZGluYXRlIHBhaXIgW3ggeV0gKGlu
IHBpeGVscykgYW5kIHRoZSBuYW1lIG9mIGEgcmVzb3VyY2UNCiAgICAoZnJvbSBsaXN0X3Jlc291
cmNlcyBjb21tYW5kKSBvcGVuIGEgdmlld2VyIG9uIHRoYXQgcmVzb3VyY2UgYXQgdGhhdA0KICAg
IGxvY2F0aW9uLg0KICAgICcnJw0KICAgICgoeCwgKHksIF8pKSwgKG5hbWUsIHN0YWNrKSkgPSBz
dGFjaw0KICAgIG9tID0gY29yZS5PcGVuTWVzc2FnZSh3b3JsZCwgbmFtZSkNCiAgICBkLmJyb2Fk
Y2FzdChvbSkNCiAgICBpZiBvbS5zdGF0dXMgPT0gY29yZS5TVUNDRVNTOg0KICAgICAgICBWID0g
ZC5vcGVuX3ZpZXdlcih4LCB5LCB0ZXh0X3ZpZXdlci5UZXh0Vmlld2VyKQ0KICAgICAgICBWLmNv
bnRlbnRfaWQsIFYubGluZXMgPSBvbS5jb250ZW50X2lkLCBvbS50aGluZw0KICAgICAgICBWLmRy
YXcoKQ0KICAgIHJldHVybiBzdGFjaw0KDQoNCkBpbnN0YWxsDQpAU2ltcGxlRnVuY3Rpb25XcmFw
cGVyDQpkZWYgbmFtZV92aWV3ZXIoc3RhY2spOg0KICAgICcnJw0KICAgIEdpdmVuIGEgc3RyaW5n
IG5hbWUgb24gdGhlIHN0YWNrLCBpZiB0aGUgY3VycmVudGx5IGZvY3VzZWQgdmlld2VyIGlzDQog
ICAgYW5vbnltb3VzLCBuYW1lIHRoZSB2aWV3ZXIgYW5kIHBlcnNpc3QgaXQgaW4gdGhlIHJlc291
cmNlIHN0b3JlIHVuZGVyDQogICAgdGhhdCBuYW1lLg0KICAgICcnJw0KICAgIG5hbWUsIHN0YWNr
ID0gc3RhY2sNCiAgICBhc3NlcnQgaXNpbnN0YW5jZShuYW1lLCBzdHIpLCByZXByKG5hbWUpDQog
ICAgaWYgZC5mb2N1c2VkX3ZpZXdlciBhbmQgbm90IGQuZm9jdXNlZF92aWV3ZXIuY29udGVudF9p
ZDoNCiAgICAgICAgZC5mb2N1c2VkX3ZpZXdlci5jb250ZW50X2lkID0gbmFtZQ0KICAgICAgICBw
bSA9IGNvcmUuUGVyc2lzdE1lc3NhZ2Uod29ybGQsIG5hbWUsIHRoaW5nPWQuZm9jdXNlZF92aWV3
ZXIubGluZXMpDQogICAgICAgIGQuYnJvYWRjYXN0KHBtKQ0KICAgICAgICBkLmZvY3VzZWRfdmll
d2VyLmRyYXdfbWVudSgpDQogICAgcmV0dXJuIHN0YWNrDQoNCg0KIyNAaW5zdGFsbA0KIyNAU2lt
cGxlRnVuY3Rpb25XcmFwcGVyDQojI2RlZiBwZXJzaXN0X3ZpZXdlcihzdGFjayk6DQojIyAgICBp
ZiBzZWxmLmZvY3VzZWRfdmlld2VyOg0KIyMgICAgICAgIA0KIyMgICAgICAgIHNlbGYuZm9jdXNl
ZF92aWV3ZXIuY29udGVudF9pZCA9IG5hbWUNCiMjICAgICAgICBzZWxmLmZvY3VzZWRfdmlld2Vy
LmRyYXdfbWVudSgpDQojIyAgICByZXR1cm4gc3RhY2sNCg0KDQpAaW5zdGFsbA0KQFNpbXBsZUZ1
bmN0aW9uV3JhcHBlcg0KZGVmIGluc2NyaWJlKHN0YWNrKToNCiAgICAnJycNCiAgICBDcmVhdGUg
YSBuZXcgSm95IGZ1bmN0aW9uIGRlZmluaXRpb24gaW4gdGhlIEpveSBkaWN0aW9uYXJ5LiAgQQ0K
ICAgIGRlZmluaXRpb24gaXMgZ2l2ZW4gYXMgYSBzdHJpbmcgd2l0aCBhIG5hbWUgZm9sbG93ZWQg
YnkgYSBkb3VibGUNCiAgICBlcXVhbCBzaWduIHRoZW4gb25lIG9yIG1vcmUgSm95IGZ1bmN0aW9u
cywgdGhlIGJvZHkuIGZvciBleGFtcGxlOg0KDQogICAgICAgIHNxciA9PSBkdXAgbXVsDQoNCiAg
ICBJZiB5b3Ugd2FudCB0aGUgZGVmaW5pdGlvbiB0byBwZXJzaXN0IG92ZXIgcmVzdGFydHMsIGVu
dGVyIGl0IGludG8NCiAgICB0aGUgZGVmaW5pdGlvbnMudHh0IHJlc291cmNlLg0KICAgICcnJw0K
ICAgIGRlZmluaXRpb24sIHN0YWNrID0gc3RhY2sNCiAgICBEZWZpbml0aW9uV3JhcHBlci5hZGRf
ZGVmKGRlZmluaXRpb24sIEQpDQogICAgcmV0dXJuIHN0YWNrDQoNCg0KQGluc3RhbGwNCkBTaW1w
bGVGdW5jdGlvbldyYXBwZXINCmRlZiBvcGVuX3ZpZXdlcihzdGFjayk6DQogICAgJycnDQogICAg
R2l2ZW4gYSBjb29yZGluYXRlIHBhaXIgW3ggeV0gKGluIHBpeGVscykgYW5kIGEgc3RyaW5nLCBv
cGVuIGEgbmV3DQogICAgdW5uYW1lZCB2aWV3ZXIgb24gdGhhdCBzdHJpbmcgYXQgdGhhdCBsb2Nh
dGlvbi4NCiAgICAnJycNCiAgICAoKHgsICh5LCBfKSksIChjb250ZW50LCBzdGFjaykpID0gc3Rh
Y2sNCiAgICBWID0gZC5vcGVuX3ZpZXdlcih4LCB5LCB0ZXh0X3ZpZXdlci5UZXh0Vmlld2VyKQ0K
ICAgIFYubGluZXMgPSBjb250ZW50LnNwbGl0bGluZXMoKQ0KICAgIFYuZHJhdygpDQogICAgcmV0
dXJuIHN0YWNrDQoNCg0KQGluc3RhbGwNCkBTaW1wbGVGdW5jdGlvbldyYXBwZXINCmRlZiBnb29k
X3ZpZXdlcl9sb2NhdGlvbihzdGFjayk6DQogICAgJycnDQogICAgTGVhdmUgYSBjb29yZGluYXRl
IHBhaXIgW3ggeV0gKGluIHBpeGVscykgb24gdGhlIHN0YWNrIHRoYXQgd291bGQNCiAgICBiZSBh
IGdvb2QgbG9jYXRpb24gYXQgd2hpY2ggdG8gb3BlbiBhIG5ldyB2aWV3ZXIuICAoVGhlIGhldXJp
c3RpYw0KICAgIGVtcGxveWVkIGlzIHRvIHRha2UgdXAgdGhlIGJvdHRvbSBoYWxmIG9mIHRoZSBj
dXJyZW50bHkgb3BlbiB2aWV3ZXINCiAgICB3aXRoIHRoZSBncmVhdGVzdCBhcmVhLikNCiAgICAn
JycNCiAgICB2aWV3ZXJzID0gbGlzdChkLml0ZXJfdmlld2VycygpKQ0KICAgIGlmIHZpZXdlcnM6
DQogICAgICAgIHZpZXdlcnMuc29ydChrZXk9bGFtYmRhIChWLCB4LCB5KTogVi53ICogVi5oKQ0K
ICAgICAgICBWLCB4LCB5ID0gdmlld2Vyc1stMV0NCiAgICAgICAgY29vcmRzID0gKHggKyAxLCAo
eSArIFYuaCAvIDIsICgpKSkNCiAgICBlbHNlOg0KICAgICAgICBjb29yZHMgPSAoMCwgKDAsICgp
KSkNCiAgICByZXR1cm4gY29vcmRzLCBzdGFjaw0KDQoNCkBpbnN0YWxsDQpARnVuY3Rpb25XcmFw
cGVyDQpkZWYgY21wXyhzdGFjaywgZXhwcmVzc2lvbiwgZGljdGlvbmFyeSk6DQogICAgJycnDQog
ICAgVGhlIGNtcCBjb21iaW5hdG9yIHRha2VzIHR3byB2YWx1ZXMgYW5kIHRocmVlIHF1b3RlZCBw
cm9ncmFtcyBvbiB0aGUNCiAgICBzdGFjayBhbmQgcnVucyBvbmUgb2YgdGhlIHRocmVlIGRlcGVu
ZGluZyBvbiB0aGUgcmVzdWx0cyBvZiBjb21wYXJpbmcNCiAgICB0aGUgdHdvIHZhbHVlczoNCg0K
ICAgICAgICAgICBhIGIgW0ddIFtFXSBbTF0gY21wDQogICAgICAgIC0tLS0tLS0tLS0tLS0tLS0t
LS0tLS0tLS0gYSA+IGINCiAgICAgICAgICAgICAgICBHDQoNCiAgICAgICAgICAgYSBiIFtHXSBb
RV0gW0xdIGNtcA0KICAgICAgICAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIGEgPSBiDQogICAg
ICAgICAgICAgICAgICAgIEUNCg0KICAgICAgICAgICBhIGIgW0ddIFtFXSBbTF0gY21wDQogICAg
ICAgIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gYSA8IGINCiAgICAgICAgICAgICAgICAgICAg
ICAgIEwNCg0KICAgICcnJw0KICAgIEwsIChFLCAoRywgKGIsIChhLCBzdGFjaykpKSkgPSBzdGFj
aw0KICAgIGV4cHJlc3Npb24gPSBjb25jYXQoRyBpZiBhID4gYiBlbHNlIEwgaWYgYSA8IGIgZWxz
ZSBFLCBleHByZXNzaW9uKQ0KICAgIHJldHVybiBzdGFjaywgZXhwcmVzc2lvbiwgZGljdGlvbmFy
eQ0KDQoNCkBpbnN0YWxsDQpAU2ltcGxlRnVuY3Rpb25XcmFwcGVyDQpkZWYgbGlzdF92aWV3ZXJz
KHN0YWNrKToNCiAgICAnJycNCiAgICBQdXQgYSBzdHJpbmcgb24gdGhlIHN0YWNrIHdpdGggc29t
ZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgY3VycmVudGx5DQogICAgb3BlbiB2aWV3ZXJzLCBvbmUt
cGVyLWxpbmUuICBUaGlzIGlzIGtpbmQgb2YgYSBkZW1vIGZ1bmN0aW9uLCByYXRoZXINCiAgICB0
aGFuIHNvbWV0aGluZyByZWFsbHkgdXNlZnVsLg0KICAgICcnJw0KICAgIGxpbmVzID0gW10NCiAg
ICBmb3IgeCwgVCBpbiBkLnRyYWNrczoNCiAgICAgICAgI2xpbmVzLmFwcGVuZCgneDogJWksIHc6
ICVpLCAlcicgJSAoeCwgVC53LCBUKSkNCiAgICAgICAgZm9yIHksIFYgaW4gVC52aWV3ZXJzOg0K
ICAgICAgICAgICAgbGluZXMuYXBwZW5kKCd4OiAlaSB5OiAlaSBoOiAlaSAlciAlcicgJSAoeCwg
eSwgVi5oLCBWLmNvbnRlbnRfaWQsIFYpKQ0KICAgIHJldHVybiAnXG4nLmpvaW4obGluZXMpLCBz
dGFjaw0KDQoNCkBpbnN0YWxsDQpAU2ltcGxlRnVuY3Rpb25XcmFwcGVyDQpkZWYgc3BsaXRsaW5l
cyhzdGFjayk6DQogICAgJycnDQogICAgR2l2ZW4gYSBzdHJpbmcgb24gdGhlIHN0YWNrIHJlcGxh
Y2UgaXQgd2l0aCBhIGxpc3Qgb2YgdGhlIGxpbmVzIGluDQogICAgdGhlIHN0cmluZy4NCiAgICAn
JycNCiAgICB0ZXh0LCBzdGFjayA9IHN0YWNrDQogICAgYXNzZXJ0IGlzaW5zdGFuY2UodGV4dCwg
c3RyKSwgcmVwcih0ZXh0KQ0KICAgIHJldHVybiBsaXN0X3RvX3N0YWNrKHRleHQuc3BsaXRsaW5l
cygpKSwgc3RhY2sNCg0KDQpAaW5zdGFsbA0KQFNpbXBsZUZ1bmN0aW9uV3JhcHBlcg0KZGVmIGhp
eWEoc3RhY2spOg0KICAgICcnJw0KICAgIERlbW8gZnVuY3Rpb24gdG8gaW5zZXJ0ICJIaSBXb3Js
ZCEiIGludG8gdGhlIGN1cnJlbnQgdmlld2VyLCBpZiBhbnkuDQogICAgJycnDQogICAgaWYgZC5m
b2N1c2VkX3ZpZXdlcjoNCiAgICAgICAgZC5mb2N1c2VkX3ZpZXdlci5pbnNlcnQoJ0hpIFdvcmxk
IScpDQogICAgcmV0dXJuIHN0YWNrDQpQSwMEFAAAAAAA5GZ4TkXs5NYLAAAACwAAAAcAAABsb2cu
dHh0Sm95cHkgbG9nDQpQSwMEFAAAAAAA5GZ4Tmf2u80CBQAAAgUAAAgAAABtZW51LnR4dCAgbmFt
ZV92aWV3ZXINCiAgbGlzdF9yZXNvdXJjZXMNCiAgb3Blbl9yZXNvdXJjZV9hdF9nb29kX2xvY2F0
aW9uDQogIGdvb2Rfdmlld2VyX2xvY2F0aW9uDQogIG9wZW5fdmlld2VyDQogIHNlZV9zdGFjaw0K
ICBzZWVfcmVzb3VyY2VzDQogIHNlZV9kZWZpbml0aW9ucw0KICBzZWVfbG9nDQogIHJlc2V0X2xv
Zw0KDQogIGluc2NyaWJlDQogIGV2YWx1YXRlDQoNCiAgcG9wIGNsZWFyICAgIGR1cCBzd2FwDQoN
CiAgYWRkIHN1YiBtdWwgZGl2IHRydWVkaXYgbW9kdWx1cyBkaXZtb2QNCiAgcG0gKysgLS0gc3Vt
IHByb2R1Y3QgcG93IHNxciBzcXJ0DQogIDwgPD0gPSA+PSA+IDw+DQogICYgPDwgPj4NCg0KICBp
IGR1cGRpcA0KDQohPSAlICYgKiAqZnJhY3Rpb24gKmZyYWN0aW9uMCArICsrIC0gLS0gLyA8IDw8
IDw9IDw+ID0gPiA+PSA+PiA/IF4NCmFicyBhZGQgYW5hbW9ycGhpc20gYW5kIGFwcDEgYXBwMiBh
cHAzIGF0IGF2ZXJhZ2UNCmIgYmluYXJ5IGJyYW5jaA0KY2hvaWNlIGNsZWFyIGNsZWF2ZSBjb25j
YXQgY29ucw0KZGluZnJpcnN0IGRpcCBkaXBkIGRpcGRkIGRpc2Vuc3RhY2tlbiBkaXYgZGl2bW9k
IGRvd25fdG9femVybyBkcm9wDQpkdWRpcGQgZHVwIGR1cGQgZHVwZGlwDQplbnN0YWNrZW4gZXEN
CmZpcnN0IGZsYXR0ZW4gZmxvb3IgZmxvb3JkaXYNCmdjZCBnZSBnZW5yZWMgZ2V0aXRlbSBncmFu
ZF9yZXNldCBndA0KaGVscA0KaSBpZCBpZnRlIGluZnJhIGluc2NyaWJlDQprZXlfYmluZGluZ3MN
CmxlIGxlYXN0X2ZyYWN0aW9uIGxvb3AgbHNoaWZ0IGx0DQptYXAgbWF4IG1pbiBtb2QgbW9kdWx1
cyBtb3VzZV9iaW5kaW5ncyBtdWwNCm5lIG5lZyBub3QgbnVsbGFyeQ0Kb2Ygb3Igb3Zlcg0KcGFt
IHBhcnNlIHBpY2sgcG0gcG9wIHBvcGQgcG9wZGQgcG9wb3AgcG93IHByZWQgcHJpbXJlYyBwcm9k
dWN0DQpxdW90ZWQNCnJhbmdlIHJhbmdlX3RvX3plcm8gcmVtIHJlbWFpbmRlciByZW1vdmUgcmVz
ZXRfbG9nIHJlc3QgcmV2ZXJzZQ0Kcm9sbDwgcm9sbD4gcm9sbGRvd24gcm9sbHVwIHJzaGlmdCBy
dW4NCnNlY29uZCBzZWxlY3Qgc2hhcmluZyBzaG93X2xvZyBzaHVudCBzaXplIHNvcnQgc3FyIHNx
cnQgc3RhY2sgc3RlcA0Kc3RlcF96ZXJvIHN1YiBzdWNjIHN1bSBzd2FhY2sgc3dhcCBzd29uY2F0
IHN3b25zDQp0YWtlIHRlcm5hcnkgdGhpcmQgdGltZXMgdHJ1ZWRpdiB0cnV0aHkgdHVjaw0KdW5h
cnkgdW5jb25zIHVuaXF1ZSB1bml0IHVucXVvdGVkIHVuc3RhY2sNCnZvaWQNCndhcnJhbnR5IHdo
aWxlIHdvcmRzDQp4IHhvcg0KemlwDQpQSwMEFAAAAAAA5GZ4TgCrPcaOEAAAjhAAAAsAAABzY3Jh
dGNoLnR4dFdoYXQgaXMgaXQ/DQoNCkEgc2ltcGxlIEdyYXBoaWNhbCBVc2VyIEludGVyZmFjZSBm
b3IgdGhlIEpveSBwcm9ncmFtbWluZyBsYW5ndWFnZSwNCndyaXR0ZW4gdXNpbmcgUHlnYW1lIHRv
IGJ5cGFzcyBYMTEgZXQuIGFsLiwgbW9kZWxlZCBvbiB0aGUgT2Jlcm9uIE9TLCBhbmQNCmludGVu
ZGVkIHRvIGJlIGp1c3QgZnVuY3Rpb25hbCBlbm91Z2ggdG8gc3VwcG9ydCBib290c3RyYXBwaW5n
IGZ1cnRoZXIgSm95DQpkZXZlbG9wbWVudC4NCg0KSXQncyBiYXNpYyBmdW5jdGlvbmFsaXR5IGlz
IG1vcmUtb3ItbGVzcyBhcyBhIGNydWRlIHRleHQgZWRpdG9yIGFsb25nIHdpdGgNCmEgc2ltcGxl
IEpveSBydW50aW1lIChpbnRlcnByZXRlciwgc3RhY2ssIGFuZCBkaWN0aW9uYXJ5LikgIEl0IGF1
dG8tIHNhdmVzDQphbnkgbmFtZWQgZmlsZXMgKGluIGEgdmVyc2lvbmVkIGhvbWUgZGlyZWN0b3J5
KSBhbmQgeW91IGNhbiB3cml0ZSBuZXcgSm95DQpwcmltaXRpdmVzIGluIFB5dGhvbiBhbmQgSm95
IGRlZmluaXRpb25zIGFuZCBpbW1lZGlhdGVseSBpbnN0YWxsIGFuZCB1c2UNCnRoZW0sIGFzIHdl
bGwgYXMgcmVjb3JkaW5nIHRoZW0gZm9yIHJldXNlIChhZnRlciByZXN0YXJ0cy4pDQoNCkN1cnJl
bnRseSwgdGhlcmUgYXJlIG9ubHkgdHdvIGtpbmRzIG9mIChpbnRlcmVzdGluZykgdmlld2Vyczog
VGV4dFZpZXdlcnMNCmFuZCBTdGFja1ZpZXdlci4gVGhlIFRleHRWaWV3ZXJzIGFyZSBjcnVkZSB0
ZXh0IGVkaXRvcnMuICBUaGV5IHByb3ZpZGUNCmp1c3QgZW5vdWdoIGZ1bmN0aW9uYWxpdHkgdG8g
bGV0IHRoZSB1c2VyIHdyaXRlIHRleHQgYW5kIGNvZGUgKFB5dGhvbiBhbmQNCkpveSkgYW5kIGV4
ZWN1dGUgSm95IGZ1bmN0aW9ucy4gIE9uZSBpbXBvcnRhbnQgdGhpbmcgdGhleSBkbyBpcw0KYXV0
b21hdGljYWxseSBzYXZlIHRoZWlyIGNvbnRlbnQgYWZ0ZXIgY2hhbmdlcy4gIE5vIG1vcmUgbG9z
dCB3b3JrLg0KDQpUaGUgU3RhY2tWaWV3ZXIgaXMgYSBzcGVjaWFsaXplZCBUZXh0Vmlld2VyIHRo
YXQgc2hvd3MgdGhlIGNvbnRlbnRzIG9mIHRoZQ0KSm95IHN0YWNrIG9uZSBsaW5lIHBlciBzdGFj
ayBpdGVtLiAgSXQncyBhIHZlcnkgaGFuZHkgdmlzdWFsIGFpZCB0byBrZWVwDQp0cmFjayBvZiB3
aGF0J3MgZ29pbmcgb24uICBUaGVyZSdzIGFsc28gYSBsb2cudHh0IGZpbGUgdGhhdCBnZXRzIHdy
aXR0ZW4NCnRvIHdoZW4gY29tbWFuZHMgYXJlIGV4ZWN1dGVkLCBhbmQgc28gcmVjb3JkcyB0aGUg
bG9nIG9mIHVzZXIgYWN0aW9ucyBhbmQNCnN5c3RlbSBldmVudHMuICBJdCB0ZW5kcyB0byBmaWxs
IHVwIHF1aWNrbHkgc28gdGhlcmUncyBhIHJlc2V0X2xvZyBjb21tYW5kDQp0aGF0IGNsZWFycyBp
dCBvdXQuDQoNClZpZXdlcnMgaGF2ZSAiZ3JvdyIgYW5kICJjbG9zZSIgaW4gdGhlaXIgbWVudSBi
YXJzLiAgVGhlc2UgYXJlIGJ1dHRvbnMuDQpXaGVuIHlvdSByaWdodC1jbGljayBvbiBncm93IGEg
dmlld2VyIGEgY29weSBpcyBjcmVhdGVkIHRoYXQgY292ZXJzIHRoYXQNCnZpZXdlcidzIGVudGly
ZSB0cmFjay4gIElmIHlvdSBncm93IGEgdmlld2VyIHRoYXQgYWxyZWFkeSB0YWtlcyB1cCBpdHMN
Cndob2xlIHRyYWNrIHRoZW4gYSBjb3B5IGlzIGNyZWF0ZWQgdGhhdCB0YWtlcyB1cCBhbiBhZGRp
dGlvbmFsIHRyYWNrLCB1cA0KdG8gdGhlIHdob2xlIHNjcmVlbi4gIENsb3NpbmcgYSB2aWV3ZXIg
anVzdCBkZWxldGVzIHRoYXQgdmlld2VyLCBhbmQgd2hlbg0KYSB0cmFjayBoYXMgbm8gbW9yZSB2
aWV3ZXJzLCBpdCBpcyBkZWxldGVkIGFuZCB0aGF0IGV4cG9zZXMgYW55IHByZXZpb3VzDQp0cmFj
a3MgYW5kIHZpZXdlcnMgdGhhdCB3ZXJlIGhpZGRlbi4NCg0KKE5vdGU6IGlmIHlvdSBldmVyIGNs
b3NlIGFsbCB0aGUgdmlld2VycyBhbmQgYXJlIHNpdHRpbmcgYXQgYSBibGFuayBzY3JlZW4NCndp
dGggIG5vd2hlcmUgdG8gdHlwZSBhbmQgZXhlY3V0ZSBjb21tYW5kcywgcHJlc3MgdGhlIFBhdXNl
L0JyZWFrIGtleS4NClRoaXMgd2lsbCBvcGVuIGEgbmV3ICJ0cmFwIiB2aWV3ZXIgd2hpY2ggeW91
IGNhbiB0aGVuIHVzZSB0byByZWNvdmVyLikNCg0KQ29waWVzIG9mIGEgdmlld2VyIGFsbCBzaGFy
ZSB0aGUgc2FtZSBtb2RlbCBhbmQgdXBkYXRlIHRoZWlyIGRpc3BsYXkgYXMgaXQNCmNoYW5nZXMu
IChJZiB5b3UgaGF2ZSB0d28gdmlld2VycyBvcGVuIG9uIHRoZSBzYW1lIG5hbWVkIHJlc291cmNl
IGFuZCBlZGl0DQpvbmUgeW91J2xsIHNlZSB0aGUgb3RoZXIgdXBkYXRlIGFzIHlvdSB0eXBlLikN
Cg0KVUkgR3VpZGUNCg0KbGVmdCBtb3VzZSBzZXRzIGN1cnNvciBpbiB0ZXh0LCBpbiBtZW51IGJh
ciByZXNpemVzIHZpZXdlciBpbnRlcmFjdGl2ZWx5DQoodGhpcyBpcyBhIGxpdHRsZSBidWdneSBp
biB0aGF0IHlvdSBjYW4gbW92ZSB0aGUgbW91c2UgcXVpY2tseSBhbmQgZ2V0DQpvdXRzaWRlIHRo
ZSBtZW51LCBsZWF2aW5nIHRoZSB2aWV3ZXIgaW4gdGhlICJyZXNpemluZyIgc3RhdGUuIFVudGls
IEkgZml4DQp0aGlzLCB0aGUgd29ya2Fyb3VuZCBpcyB0byBqdXN0IGdyYWIgdGhlIG1lbnUgYmFy
IGFnYWluIGFuZCB3aWdnbGUgaXQgYQ0KZmV3IHBpeGVscyBhbmQgbGV0IGdvLiAgVGhpcyB3aWxs
IHJlc2V0IHRoZSBtYWNoaW5lcnkuKQ0KDQpSaWdodCBtb3VzZSBleGVjdXRlcyBKb3kgY29tbWFu
ZCAoZnVuY3Rpb25zKSwgYW5kIHlvdSBjYW4gZHJhZyB3aXRoIHRoZQ0KcmlnaHQgYnV0dG9uIHRv
IGhpZ2hsaWdodCAod2VsbCwgdW5kZXJsaW5lKSBjb21tYW5kcy4gIFdvcmRzIHRoYXQgYXJlbid0
DQpuYW1lcyBvZiBKb3kgY29tbWFuZHMgd29uJ3QgYmUgdW5kZXJsaW5lZC4gIFJlbGVhc2UgdGhl
IGJ1dHRvbiB0byBleGVjdXRlDQp0aGUgY29tbWFuZC4NCg0KVGhlIG1pZGRsZSBtb3VzZSBidXR0
b24gKHVzdWFsbHkgYSB3aGVlbCB0aGVzZSBkYXlzKSBzY3JvbGxzIHRoZSB0ZXh0IGJ1dA0KeW91
IGNhbiBhbHNvIGNsaWNrIGFuZCBkcmFnIGFueSB2aWV3ZXIgd2l0aCBpdCB0byBtb3ZlIHRoYXQg
dmlld2VyIHRvDQphbm90aGVyIHRyYWNrIG9yIHRvIGEgZGlmZmVyZW50IGxvY2F0aW9uIGluIHRo
ZSBzYW1lIHRyYWNrLiAgVGhlcmUncyBubw0KZGlyZWN0IHZpc3VhbCBmZWVkYmFjayBmb3IgdGhp
cyAoeWV0KSBidXQgdGhhdCBkb3Nlbid0IHNlZW0gdG8gaW1wYWlyIGl0cw0KdXNlZnVsbmVzcy4N
Cg0KRjEsIEYyIC0gc2V0IHNlbGVjdGlvbiBiZWdpbiBhbmQgZW5kIG1hcmtlcnMgKGNydWRlIGJ1
dCB1c2FibGUuKQ0KDQpGMyAtIGNvcHkgc2VsZWN0ZWQgdGV4dCB0byB0aGUgdG9wIG9mIHRoZSBz
dGFjay4NCg0KU2hpZnQtRjMgLSBhcyBjb3B5IHRoZW4gcnVuICJwYXJzZSIgY29tbWFuZCBvbiB0
aGUgc3RyaW5nLg0KDQpGNCAtIGN1dCBzZWxlY3RlZCB0ZXh0IHRvIHRoZSB0b3Agb2YgdGhlIHN0
YWNrLg0KDQpTaGlmdC1GNCAtIGFzIGN1dCB0aGVuIHJ1biAicG9wIiAoZGVsZXRlIHNlbGVjdGlv
bi4pDQoNCkpveQ0KDQpQcmV0dHkgbXVjaCBhbGwgb2YgdGhlIHJlc3Qgb2YgdGhlIGZ1bmN0aW9u
YWxpdHkgb2YgdGhlIHN5c3RlbSBpcyBwcm92aWRlZA0KYnkgZXhlY3V0aW5nIEpveSBjb21tYW5k
cyAoYWthIGZ1bmN0aW9ucywgYWthICJ3b3JkcyIgaW4gRm9ydGgpIGJ5IHJpZ2h0LQ0KY2xpY2tp
bmcgb24gdGhlaXIgbmFtZXMgaW4gYW55IHRleHQuDQoNClRvIGdldCBoZWxwIG9uIGEgSm95IGZ1
bmN0aW9uIHNlbGVjdCB0aGUgbmFtZSBvZiB0aGUgZnVuY3Rpb24gaW4gYQ0KVGV4dFZpZXdlciB1
c2luZyBGMSBhbmQgRjIsIHRoZW4gcHJlc3Mgc2hpZnQtRjMgdG8gcGFyc2UgdGhlIHNlbGVjdGlv
bi4NClRoZSBmdW5jdGlvbiAocmVhbGx5IGl0cyBTeW1ib2wpIHdpbGwgYXBwZWFyIG9uIHRoZSBz
dGFjayBpbiBicmFja2V0cyAoYQ0KInF1b3RlZCBwcm9ncmFtIiBzdWNoIGFzICJbcG9wXSIuKSAg
VGhlbiByaWdodC1jbGljayBvbiB0aGUgd29yZCBoZWxwIGluDQphbnkgVGV4dFZpZXdlciAoaWYg
aXQncyBub3QgYWxyZWFkeSB0aGVyZSwganVzdCB0eXBlIGl0IGluIHNvbWV3aGVyZS4pDQpUaGlz
IHdpbGwgcHJpbnQgdGhlIGRvY3N0cmluZyBvciBkZWZpbml0aW9uIG9mIHRoZSB3b3JkIChmdW5j
dGlvbikgdG8NCnN0ZG91dC4gIEF0IHNvbWUgcG9pbnQgSSdsbCB3cml0ZSBhIHRoaW5nIHRvIHNl
bmQgdGhhdCB0byB0aGUgbG9nLnR4dCBmaWxlDQppbnN0ZWFkLCBidXQgZm9yIG5vdyBsb29rIGZv
ciBvdXRwdXQgaW4gdGhlIHRlcm1pbmFsLg0KUEsDBBQAAAAAAORmeE53f5peAwAAAAMAAAAMAAAA
c3RhY2sucGlja2xlKHQuUEsBAhQAFAAAAAAA5GZ4Tv3gGVF+AwAAfgMAAA8AAAAAAAAAAAAAALaB
AAAAAGRlZmluaXRpb25zLnR4dFBLAQIUABQAAAAAACFrpk7/HHjxGBYAABgWAAAKAAAAAAAAAAAA
AAC2gasDAABsaWJyYXJ5LnB5UEsBAhQAFAAAAAAA5GZ4TkXs5NYLAAAACwAAAAcAAAAAAAAAAAAA
ALaB6xkAAGxvZy50eHRQSwECFAAUAAAAAADkZnhOZ/a7zQIFAAACBQAACAAAAAAAAAAAAAAAtoEb
GgAAbWVudS50eHRQSwECFAAUAAAAAADkZnhOAKs9xo4QAACOEAAACwAAAAAAAAAAAAAAtoFDHwAA
c2NyYXRjaC50eHRQSwECFAAUAAAAAADkZnhOd3+aXgMAAAADAAAADAAAAAAAAAAAAAAAtoH6LwAA
c3RhY2sucGlja2xlUEsFBgAAAAAGAAYAUwEAACcwAAAAAA==''')))


if __name__ == '__main__':
    print create_data()