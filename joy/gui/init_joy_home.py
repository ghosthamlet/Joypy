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
UEsDBBQAAAAAAKW29EyLEfLTUQgAAFEIAAALAAAAc2NyYXRjaC50eHRyZXNldF9sb2cgd29yZHMg
bW91c2VfYmluZGluZ3Mga2V5X2JpbmRpbmdzCgpTdGFjayBDaGF0dGVyCgogZHVwIGR1cGQgZHVw
ZGQgb3ZlciB0dWNrCiBwb3AgcG9wZCBwb3BkZCBwb3BvcCBwb3BvcGQgcG9wb3BkZAogc3dhcCBy
b2xsPCByb2xsPiByb2xsZG93biByb2xsdXAgCiB1bml0IGNsZWFyCgpNYXRoCgogYWRkICsgc3Vi
IC0gbXVsICogdHJ1ZWRpdiAvIG1vZCAlCiBkaXYgZGl2bW9kIGZsb29yIHBtCiBhYnMgc3FyIHNx
cnQgbmVnIHBvdwogbWF4IG1pbiBzdW0gYXZlcmFnZSBwcm9kdWN0CiBwcmVkIC0tIHN1Y2MgKysg
bHNoaWZ0IDw8IHJzaGlmdCA+PgoKTG9naWMKCiBnZSBndCBlcSBsZSBsdCBuZQogIDwgPD0gPSAg
Pj0gPiAgIT0gPD4KIGFuZCAmIG9yIG5vdCB4b3IgXgogYm9vbCB0cnV0aHkgPwoKQ29tYmluYXRv
cnMKCiBpIHggYiBpbmZyYSBkaXAgZGlwZCBkaXBkZCBkdXBkaXAgZHVwZGlwZAogY2xlYXZlIGZv
cmsgYXBwMSBhcHAyIGFwcDMgbWFwIHBhbQogbnVsbGFyeSB1bmFyeSBiaW5hcnkgdGVybmFyeSAK
CkNvbnRyb2wgRmxvdwoKIGJyYW5jaCBjb25kIGlmdGUgY2hvaWNlCiBsb29wIHdoaWxlIGdlbnJl
YyBwcmltcmVjCiBtYWtlX2dlbmVyYXRvcgoKTGlzdCBNYW5pcHVsYXRpb24KCiBlbnN0YWNrZW4g
ZGlzZW5zdGFja2VuIHN0YWNrIHVuc3RhY2sKIGZpcnN0IGZpcnN0X3R3byBzZWNvbmQgdGhpcmQg
Zm91cnRoIHJlc3QgcnJlc3QKIGZsYXR0ZW4gZHJvcCB0YWtlIHJldmVyc2Ugc2VsZWN0IHppcAog
c2l6ZSBzb3J0IHNodW50IGdldGl0ZW0KIHN0ZXAgc3RlcF96ZXJvIHRpbWVzIAogY29ucyBjY29u
cyB1bmNvbnMgc3dvbnMgdW5zd29ucwogY29uY2F0IHVuaXF1ZQogcmVtb3ZlCiBhdCBvZiBwaWNr
CiB1bnF1b3RlZCBxdW90ZWQKCk1pc2MKCiBkb3duX3RvX3plcm8gY21wIGdjZCBoZWxwIGlkIAog
bGVhc3RfZnJhY3Rpb24gcGFyc2UgcXVvdGVkCiByYW5nZSByYW5nZV90b196ZXJvCiByZXNldF9s
b2cgIHNob3dfbG9nCiBydW4gCiBzdHVuY29ucyBzdHVudW5jb25zCiBzd2FhY2sgCiB2b2lkICAg
ICAKCgpbIF0gQWRkIGxvZ2dpbmc/ClsgXSBJTkkgZmlsZT8KWyBdIGRlZmluaXRpb25zLnR4dApb
IF0gSW50ZWdyYXRlIGluZmVyZW5jZQpbIF0gY29tbWFuZCB0byAocmUtKXJ1biB3aXRoIHRyYWNl
ClsgXSBCYWNrdGltZSBidXR0b24/CgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t
LS0tLS0tLS0tClsyMyAxOF0gICBbdW5pdCBpXQoKc3FyICBmb28gPT0gdW5jb25zIG11bAoKIHN3
YWFjawoKIG92ZXIgW1tbbmVnXSBkdXBkaXAgc3FyIDRdIGRpcGQgKiAqIC0gc3FydCBwbV0gZGlw
IDIgKiBbL10gY29ucyBhcHAyCgo1IHNxcnQgMiAvIDAuNSArCjUgc3FydCAxICsgMiAvCnBoaSA9
PSA1IHNxcnQgKysgMiAvCnBoaSA9PSAxLjYxODAzMzk4ODc0OTg5NQooQnV0IHRoaXMgaXMgTGFt
YmRhIEFic3RhY3Rpb24gc25lYWtpbmcgaW4gdGhlIGJhY2sgZG9vci4pCj0KY2xlYXIKCihuMSBu
MiAtLSDimK8pCgoyMDE4IDIwIDE4IDIwIDIzIDAuNQo0NzIgODMgLyAtNwoxMDAKCjEwMCAqIGZs
b29yIDEwMCAvICBzaG93X2xvZwoKWzIgM10gW3N3YXAgdHJ1ZWRpdl0gaW5mcmEKCmR1cCBpbmZy
YSBrZXlfYmluZGluZ3MgZGl2bW9kCgogIDEgW2R1cCAxIDw8XSBtYWtlX2dlbmVyYXRvciAgIDIz
IFt4IHBvcGRdIHRpbWVzIGZpcnN0CgptY2M5MSA9PSBbMTAwID5dIFsxMCAtXSBbMTEgKyBtY2M5
MSBtY2M5MV0gaWZ0ZQogICAgICA9PSBbMTAwID5dIFsxMCAtXSBbMTEgKyBbbWNjOTFdIFttY2M5
MV0gYl0gaWZ0ZQogICAgICA9PSBbMTAwID5dIFsxMCAtXSBbMTEgKyBbbWNjOTFdIGR1cCBiXSBp
ZnRlCm1jYzkxID09IFsxMDAgPl0gWzEwIC1dIFsxMSArXSBbZHVwIGJdIGdlbnJlYwoKMjc5ODQx
IDIwIDIwIDIwIDIwMjMxOCAyNzk4NDEgMjc5ODQxIDI3OTg0MTI3OTg0MTIwMjAyMzE4CgppbnNj
cmliZQoKcm91bmRfdG9fY2VudHMgPT0gMTAwICogKysgZmxvb3IgMTAwIC8KCgogICAgWzEyIDE4
XSBbW3BtXSBpbmZyYV0gbWFrZV9nZW5lcmF0b3IKCiAgICBbMTIgMThdIFtbWytdIFszIC9dIGZv
cmsgcG9wb3BkZF0gaW5mcmFdIG1ha2VfZ2VuZXJhdG9yCgogICBbc3RhY2tdIFtwb3BdIHdoaWxl
CgoKClBLAwQUAAAAAABAQfVM5+RkR1EBAABRAQAABwAAAGxvZy50eHRKb3lweSAtIENvcHlyaWdo
dCDCqSAyMDE4IFNpbW9uIEZvcm1hbgpUaGlzIHByb2dyYW0gY29tZXMgd2l0aCBBQlNPTFVURUxZ
IE5PIFdBUlJBTlRZOyBmb3IgZGV0YWlscyByaWdodC1jbGljayAid2FycmFudHkiLiBUaGlzIGlz
IGZyZWUgc29mdHdhcmUsIGFuZCB5b3UgYXJlIHdlbGNvbWUgdG8gcmVkaXN0cmlidXRlIGl0IHVu
ZGVyIGNlcnRhaW4gY29uZGl0aW9uczsgcmlnaHQtY2xpY2sgInNoYXJpbmciIGZvciBkZXRhaWxz
LiBSaWdodC1jbGljayBvbiB0aGVzZSBjb21tYW5kcyB0byBzZWUgZG9jcyBvbiBVSSBjb21tYW5k
czoga2V5X2JpbmRpbmdzIG1vdXNlX2JpbmRpbmdzCgogPC0KUEsDBBQAAAAAAEFB9Ux3f5peAwAA
AAMAAAAMAAAAc3RhY2sucGlja2xlKHQuUEsDBBQAAAAAAHy09ExY7AlUJgUAACYFAAALAAAAdGh1
bi5jb25maWcKW2tleSBiaW5kaW5nc10KPEY1PiA9IHN3YXAKPEY2PiA9IGR1cAo8U2hpZnQtRjU+
ID0gcm9sbDwKPFNoaWZ0LUY2PiA9IHJvbGw+CjxGNz4gPSBvdmVyCjxTaGlmdC1GNz4gPSB0dWNr
CjxGOD4gPSBwYXJzZQo8RjEyPiA9IHdvcmRzCjxGMT4gPSByZXNldF9sb2cgc2hvd19sb2cKPEVz
Y2FwZT4gPSBjbGVhciByZXNldF9sb2cgc2hvd19sb2cKPENvbnRyb2wtRGVsZXRlPiA9IHBvcAo8
Q29udHJvbC1pPiA9IGkKCgpbRGVmaW5pdGlvbnNdCm9mID0gc3dhcCBhdApwcm9kdWN0ID0gMSBz
d2FwIFsqXSBzdGVwCmZsYXR0ZW4gPSBbXSBzd2FwIFtjb25jYXRdIHN0ZXAKcXVvdGVkID0gW3Vu
aXRdIGRpcAp1bnF1b3RlZCA9IFtpXSBkaXAKZW5zdGFja2VuID0gc3RhY2sgW2NsZWFyXSBkaXAK
PyA9IGR1cCB0cnV0aHkKZGlzZW5zdGFja2VuID0gPyBbdW5jb25zID9dIGxvb3AgcG9wCmRpbmZy
aXJzdCA9IGRpcCBpbmZyYSBmaXJzdApudWxsYXJ5ID0gW3N0YWNrXSBkaW5mcmlyc3QKdW5hcnkg
PSBudWxsYXJ5IHBvcGQKYmluYXJ5ID0gbnVsbGFyeSBbcG9wb3BdIGRpcAp0ZXJuYXJ5ID0gdW5h
cnkgW3BvcG9wXSBkaXAKcGFtID0gW2ldIG1hcApydW4gPSBbXSBzd2FwIGluZnJhCnNxciA9IGR1
cCBtdWwKc2l6ZSA9IDAgc3dhcCBbcG9wICsrXSBzdGVwCmZvcmsgPSBbaV0gYXBwMgpjbGVhdmUg
PSBmb3JrIFtwb3BkXSBkaXAKYXZlcmFnZSA9IFtzdW0gMS4wICpdIFtzaXplXSBjbGVhdmUgLwpn
Y2QgPSAxIFt0dWNrIG1vZHVsdXMgZHVwIDAgPl0gbG9vcCBwb3AKbGVhc3RfZnJhY3Rpb24gPSBk
dXAgW2djZF0gaW5mcmEgW2Rpdl0gY29uY2F0IG1hcAoqZnJhY3Rpb24gPSBbdW5jb25zXSBkaXAg
dW5jb25zIFtzd2FwXSBkaXAgY29uY2F0IFsqXSBpbmZyYSBbKl0gZGlwIGNvbnMKKmZyYWN0aW9u
MCA9IGNvbmNhdCBbW3N3YXBdIGRpcCAqIFsqXSBkaXBdIGluZnJhCmRvd25fdG9femVybyA9IFsw
ID5dIFtkdXAgLS1dIHdoaWxlCnJhbmdlX3RvX3plcm8gPSB1bml0IFtkb3duX3RvX3plcm9dIGlu
ZnJhCmFuYW1vcnBoaXNtID0gW3BvcCBbXV0gc3dhcCBbZGlwIHN3b25zXSBnZW5yZWMKcmFuZ2Ug
PSBbMCA8PV0gWzEgLSBkdXBdIGFuYW1vcnBoaXNtCndoaWxlID0gc3dhcCBbbnVsbGFyeV0gY29u
cyBkdXAgZGlwZCBjb25jYXQgbG9vcApkdXBkaXBkID0gZHVwIGRpcGQKcHJpbXJlYyA9IFtpXSBn
ZW5yZWMKc3RlcF96ZXJvID0gMCByb2xsPiBzdGVwCmNvZGlyZWNvID0gY29ucyBkaXAgcmVzdCBj
b25zCm1ha2VfZ2VuZXJhdG9yID0gW2NvZGlyZWNvXSBjY29ucwppZnRlID0gW251bGxhcnkgbm90
XSBkaXBkIGJyYW5jaAoKUEsDBBQAAAAAAEK0k0yW6MvDbQMAAG0DAAAPAAAAZGVmaW5pdGlvbnMu
dHh0c2VlX3N0YWNrID09IGdvb2Rfdmlld2VyX2xvY2F0aW9uIG9wZW5fc3RhY2sKc2VlX3Jlc291
cmNlcyA9PSBsaXN0X3Jlc291cmNlcyBnb29kX3ZpZXdlcl9sb2NhdGlvbiBvcGVuX3ZpZXdlcgpv
cGVuX3Jlc291cmNlX2F0X2dvb2RfbG9jYXRpb24gPT0gZ29vZF92aWV3ZXJfbG9jYXRpb24gb3Bl
bl9yZXNvdXJjZQpzZWVfbG9nID09ICJsb2cudHh0IiBvcGVuX3Jlc291cmNlX2F0X2dvb2RfbG9j
YXRpb24Kc2VlX2RlZmluaXRpb25zID09ICJkZWZpbml0aW9ucy50eHQiIG9wZW5fcmVzb3VyY2Vf
YXRfZ29vZF9sb2NhdGlvbgpyb3VuZF90b19jZW50cyA9PSAxMDAgKiArKyBmbG9vciAxMDAgLwpy
ZXNldF9sb2cgPT0gImRlbCBsb2cubGluZXNbMTpdIDsgbG9nLmF0X2xpbmUgPSAwIiBldmFsdWF0
ZQpzZWVfbWVudSA9PSAibWVudS50eHQiIGdvb2Rfdmlld2VyX2xvY2F0aW9uIG9wZW5fcmVzb3Vy
Y2UKCiMgT3JkZXJlZCBCaW5hcnkgVHJlZSBkYXRhc3RydWN0dXJlIGZ1bmN0aW9ucy4KQlRyZWUt
bmV3ID09IHN3YXAgW1tdIFtdXSBjb25zIGNvbnMKIF9CVHJlZS1QID09IG92ZXIgW3BvcG9wIHBv
cG9wIGZpcnN0XSBudWxsYXJ5CiBfQlRyZWUtVD4gPT0gW2NvbnMgY29ucyBkaXBkZF0gY29ucyBj
b25zIGNvbnMgaW5mcmEKIF9CVHJlZS1UPCA9PSBbY29ucyBjb25zIGRpcGRdIGNvbnMgY29ucyBj
b25zIGluZnJhCiBfQlRyZWUtRSA9PSBwb3Agc3dhcCByb2xsPCByZXN0IHJlc3QgY29ucyBjb25z
CiBfQlRyZWUtcmVjdXIgPT0gX0JUcmVlLVAgW19CVHJlZS1UPl0gW19CVHJlZS1FXSBbX0JUcmVl
LVQ8XSBjbXAKQlRyZWUtYWRkID09IFtwb3BvcCBub3RdIFtbcG9wXSBkaXBkIEJUcmVlLW5ld10g
W10gW19CVHJlZS1yZWN1cl0gZ2VucmVjClBLAQIUAxQAAAAAAKW29EyLEfLTUQgAAFEIAAALAAAA
AAAAAAAAAACAgQAAAABzY3JhdGNoLnR4dFBLAQIUAxQAAAAAAEBB9Uzn5GRHUQEAAFEBAAAHAAAA
AAAAAAAAAACAgXoIAABsb2cudHh0UEsBAhQDFAAAAAAAQUH1THd/ml4DAAAAAwAAAAwAAAAAAAAA
AAAAAICB8AkAAHN0YWNrLnBpY2tsZVBLAQIUAxQAAAAAAHy09ExY7AlUJgUAACYFAAALAAAAAAAA
AAAAAAC0gR0KAAB0aHVuLmNvbmZpZ1BLAQIUAxQAAAAAAEK0k0yW6MvDbQMAAG0DAAAPAAAAAAAA
AAAAAAC0gWwPAABkZWZpbml0aW9ucy50eHRQSwUGAAAAAAUABQAeAQAABhMAAAAA''')))


if __name__ == '__main__':
    print create_data()
