# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\7")
        buf.write("+\u011b\n+\f+\16+\u011e\13+\3,\3,\3,\3,\3-\3-\3.\6.\u0127")
        buf.write("\n.\r.\16.\u0128\3/\3/\7/\u012d\n/\f/\16/\u0130\13/\5")
        buf.write("/\u0132\n/\3\60\3\60\5\60\u0136\n\60\3\60\5\60\u0139\n")
        buf.write("\60\3\61\6\61\u013c\n\61\r\61\16\61\u013d\3\62\3\62\7")
        buf.write("\62\u0142\n\62\f\62\16\62\u0145\13\62\3\62\3\62\3\62\3")
        buf.write("\63\3\63\5\63\u014c\n\63\3\64\3\64\3\64\3\64\5\64\u0152")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u0157\n\65\3\66\3\66\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u015f\n\67\f\67\16\67\u0162\13\67\3")
        buf.write("\67\3\67\38\68\u0167\n8\r8\168\u0168\38\38\39\39\39\3")
        buf.write(":\3:\7:\u0172\n:\f:\16:\u0175\13:\3:\3:\3:\5:\u017a\n")
        buf.write(":\3:\3:\3;\3;\7;\u0180\n;\f;\16;\u0183\13;\3;\3;\3;\2")
        buf.write("\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y\2[\2]\2_\2a.c/e\2g\2i\2k\60m\61o\62q\63")
        buf.write("s\64u\65\3\2\16\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\3\2\17")
        buf.write("\17\3\2\f\f\4\2\f\f\17\17\5\2\n\13\16\17\"\"\3\3\f\f\2")
        buf.write("\u018f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\3w\3\2\2\2\5|\3\2\2\2\7\u0082\3\2\2\2\t\u0089")
        buf.write("\3\2\2\2\13\u008e\3\2\2\2\r\u0095\3\2\2\2\17\u009c\3\2")
        buf.write("\2\2\21\u00a0\3\2\2\2\23\u00a8\3\2\2\2\25\u00ad\3\2\2")
        buf.write("\2\27\u00b1\3\2\2\2\31\u00b7\3\2\2\2\33\u00ba\3\2\2\2")
        buf.write("\35\u00c0\3\2\2\2\37\u00c9\3\2\2\2!\u00cc\3\2\2\2#\u00d1")
        buf.write("\3\2\2\2%\u00d6\3\2\2\2\'\u00dc\3\2\2\2)\u00e0\3\2\2\2")
        buf.write("+\u00e4\3\2\2\2-\u00e8\3\2\2\2/\u00eb\3\2\2\2\61\u00ed")
        buf.write("\3\2\2\2\63\u00ef\3\2\2\2\65\u00f1\3\2\2\2\67\u00f3\3")
        buf.write("\2\2\29\u00f5\3\2\2\2;\u00f7\3\2\2\2=\u00fa\3\2\2\2?\u00fc")
        buf.write("\3\2\2\2A\u00fe\3\2\2\2C\u0101\3\2\2\2E\u0104\3\2\2\2")
        buf.write("G\u0107\3\2\2\2I\u010b\3\2\2\2K\u010e\3\2\2\2M\u0110\3")
        buf.write("\2\2\2O\u0112\3\2\2\2Q\u0114\3\2\2\2S\u0116\3\2\2\2U\u0118")
        buf.write("\3\2\2\2W\u011f\3\2\2\2Y\u0123\3\2\2\2[\u0126\3\2\2\2")
        buf.write("]\u0131\3\2\2\2_\u0138\3\2\2\2a\u013b\3\2\2\2c\u013f\3")
        buf.write("\2\2\2e\u014b\3\2\2\2g\u0151\3\2\2\2i\u0156\3\2\2\2k\u0158")
        buf.write("\3\2\2\2m\u015a\3\2\2\2o\u0166\3\2\2\2q\u016c\3\2\2\2")
        buf.write("s\u016f\3\2\2\2u\u017d\3\2\2\2wx\7v\2\2xy\7t\2\2yz\7w")
        buf.write("\2\2z{\7g\2\2{\4\3\2\2\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2")
        buf.write("\177\u0080\7u\2\2\u0080\u0081\7g\2\2\u0081\6\3\2\2\2\u0082")
        buf.write("\u0083\7p\2\2\u0083\u0084\7w\2\2\u0084\u0085\7o\2\2\u0085")
        buf.write("\u0086\7d\2\2\u0086\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088")
        buf.write("\b\3\2\2\2\u0089\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b")
        buf.write("\u008c\7q\2\2\u008c\u008d\7n\2\2\u008d\n\3\2\2\2\u008e")
        buf.write("\u008f\7u\2\2\u008f\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091")
        buf.write("\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093\u0094\7i\2\2\u0094")
        buf.write("\f\3\2\2\2\u0095\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\u0098\7v\2\2\u0098\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\16\3\2\2\2\u009c\u009d\7x\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7t\2\2\u009f\20\3\2\2\2\u00a0")
        buf.write("\u00a1\7f\2\2\u00a1\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7c\2\2\u00a4\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6")
        buf.write("\u00a7\7e\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9")
        buf.write("\u00aa\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac")
        buf.write("\24\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5")
        buf.write("\u00b6\7n\2\2\u00b6\30\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8")
        buf.write("\u00b9\7{\2\2\u00b9\32\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb")
        buf.write("\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be")
        buf.write("\u00bf\7m\2\2\u00bf\34\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1")
        buf.write("\u00c2\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4")
        buf.write("\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write("\u00cb\7h\2\2\u00cb \3\2\2\2\u00cc\u00cd\7g\2\2\u00cd")
        buf.write("\u00ce\7n\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\"\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7h\2\2\u00d5$\3\2\2\2\u00d6")
        buf.write("\u00d7\7d\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9")
        buf.write("\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db&\3\2\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df")
        buf.write("(\3\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2")
        buf.write("\u00e3\7v\2\2\u00e3*\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write("\u00e6\7p\2\2\u00e6\u00e7\7f\2\2\u00e7,\3\2\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7t\2\2\u00ea.\3\2\2\2\u00eb")
        buf.write("\u00ec\7-\2\2\u00ec\60\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee")
        buf.write("\62\3\2\2\2\u00ef\u00f0\7,\2\2\u00f0\64\3\2\2\2\u00f1")
        buf.write("\u00f2\7\61\2\2\u00f2\66\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f4")
        buf.write("8\3\2\2\2\u00f5\u00f6\7?\2\2\u00f6:\3\2\2\2\u00f7\u00f8")
        buf.write("\7#\2\2\u00f8\u00f9\7?\2\2\u00f9<\3\2\2\2\u00fa\u00fb")
        buf.write("\7>\2\2\u00fb>\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd@\3\2\2")
        buf.write("\2\u00fe\u00ff\7>\2\2\u00ff\u0100\7?\2\2\u0100B\3\2\2")
        buf.write("\2\u0101\u0102\7@\2\2\u0102\u0103\7?\2\2\u0103D\3\2\2")
        buf.write("\2\u0104\u0105\7?\2\2\u0105\u0106\7?\2\2\u0106F\3\2\2")
        buf.write("\2\u0107\u0108\7\60\2\2\u0108\u0109\7\60\2\2\u0109\u010a")
        buf.write("\7\60\2\2\u010aH\3\2\2\2\u010b\u010c\7>\2\2\u010c\u010d")
        buf.write("\7/\2\2\u010dJ\3\2\2\2\u010e\u010f\7]\2\2\u010fL\3\2\2")
        buf.write("\2\u0110\u0111\7_\2\2\u0111N\3\2\2\2\u0112\u0113\7*\2")
        buf.write("\2\u0113P\3\2\2\2\u0114\u0115\7+\2\2\u0115R\3\2\2\2\u0116")
        buf.write("\u0117\7.\2\2\u0117T\3\2\2\2\u0118\u011c\t\2\2\2\u0119")
        buf.write("\u011b\t\3\2\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011dV\3\2\2")
        buf.write("\2\u011e\u011c\3\2\2\2\u011f\u0120\5[.\2\u0120\u0121\5")
        buf.write("]/\2\u0121\u0122\5_\60\2\u0122X\3\2\2\2\u0123\u0124\t")
        buf.write("\4\2\2\u0124Z\3\2\2\2\u0125\u0127\5Y-\2\u0126\u0125\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129\\\3\2\2\2\u012a\u012e\7\60\2\2\u012b\u012d")
        buf.write("\5Y-\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0132\3\2\2\2\u0130")
        buf.write("\u012e\3\2\2\2\u0131\u012a\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132^\3\2\2\2\u0133\u0135\t\5\2\2\u0134\u0136\t\6\2")
        buf.write("\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0139\5[.\2\u0138\u0133\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139`\3\2\2\2\u013a\u013c\5Y-\2\u013b\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013eb\3\2\2\2\u013f\u0143\7$\2\2\u0140")
        buf.write("\u0142\5e\63\2\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3")
        buf.write("\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\7$\2\2\u0147\u0148")
        buf.write("\b\62\2\2\u0148d\3\2\2\2\u0149\u014c\n\7\2\2\u014a\u014c")
        buf.write("\5g\64\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("f\3\2\2\2\u014d\u014e\7^\2\2\u014e\u0152\t\b\2\2\u014f")
        buf.write("\u0150\7)\2\2\u0150\u0152\7$\2\2\u0151\u014d\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152h\3\2\2\2\u0153\u0157\t\t\2\2\u0154")
        buf.write("\u0155\7^\2\2\u0155\u0157\n\b\2\2\u0156\u0153\3\2\2\2")
        buf.write("\u0156\u0154\3\2\2\2\u0157j\3\2\2\2\u0158\u0159\t\n\2")
        buf.write("\2\u0159l\3\2\2\2\u015a\u015b\7%\2\2\u015b\u015c\7%\2")
        buf.write("\2\u015c\u0160\3\2\2\2\u015d\u015f\n\13\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0164\b\67\3\2\u0164n\3\2\2\2\u0165\u0167\t\f\2")
        buf.write("\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\b8\3\2\u016bp\3\2\2\2\u016c\u016d\13\2\2\2\u016d")
        buf.write("\u016e\b9\4\2\u016er\3\2\2\2\u016f\u0173\7$\2\2\u0170")
        buf.write("\u0172\5e\63\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0179\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7\17\2\2\u0177")
        buf.write("\u017a\7\f\2\2\u0178\u017a\t\r\2\2\u0179\u0176\3\2\2\2")
        buf.write("\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\b")
        buf.write(":\5\2\u017ct\3\2\2\2\u017d\u0181\7$\2\2\u017e\u0180\5")
        buf.write("e\63\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0184\u0185\5i\65\2\u0185\u0186\b;\6\2")
        buf.write("\u0186v\3\2\2\2\23\2\u011c\u0128\u012e\u0131\u0135\u0138")
        buf.write("\u013d\u0143\u014b\u0151\u0156\u0160\u0168\u0173\u0179")
        buf.write("\u0181\7\3\62\2\b\2\2\39\3\3:\4\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LT = 30
    GT = 31
    LE = 32
    GE = 33
    STR_EQ = 34
    STR_CONCAT = 35
    ASSIGNINIT = 36
    LSB = 37
    RSB = 38
    LP = 39
    RP = 40
    CM = 41
    ID = 42
    NUMBER_LIT = 43
    INTLIT = 44
    STRING_LIT = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", 
            "'...'", "'<-'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LT", "GT", 
            "LE", "GE", "STR_EQ", "STR_CONCAT", "ASSIGNINIT", "LSB", "RSB", 
            "LP", "RP", "CM", "ID", "NUMBER_LIT", "INTLIT", "STRING_LIT", 
            "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "NOT_EQUAL", "LT", "GT", "LE", "GE", "STR_EQ", "STR_CONCAT", 
                  "ASSIGNINIT", "LSB", "RSB", "LP", "RP", "CM", "ID", "NUMBER_LIT", 
                  "DIGIT", "DIGITS", "OPT_FRAC", "OPT_EXP", "INTLIT", "STRING_LIT", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "NEWLINE", "COMMENTS", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_LIT_action 
            actions[55] = self.ERROR_CHAR_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1] 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


