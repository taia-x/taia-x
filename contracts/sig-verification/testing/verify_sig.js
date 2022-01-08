"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var taquito_1 = require("@taquito/taquito");
var signer_1 = require("@taquito/signer");
function verify_sig() {
    return __awaiter(this, void 0, void 0, function () {
        var provider, signer, tezos, _a, _b, contract, _c, _d, ex_1;
        return __generator(this, function (_e) {
            switch (_e.label) {
                case 0:
                    provider = 'https://hangzhounet.api.tez.ie';
                    signer = new signer_1.InMemorySigner('edsk3JRacRgUiZY7ciHsqRbPEqBcHASQpvoHoUAvmB1uq7Fu5RHzam');
                    tezos = new taquito_1.TezosToolkit(provider);
                    tezos.setSignerProvider(signer);
                    _e.label = 1;
                case 1:
                    _e.trys.push([1, 5, , 6]);
                    console.log("signer pkh:");
                    _b = (_a = console).log;
                    return [4 /*yield*/, signer.publicKeyHash()];
                case 2:
                    _b.apply(_a, [_e.sent()]);
                    return [4 /*yield*/, tezos.contract.at('KT1QS8m9TzQF3PvJzxpDgqHYGTtBWqW3FCev')];
                case 3:
                    contract = _e.sent();
                    console.log("Printing contract methods...");
                    console.log(contract.methods);
                    console.log("Showing initial storage...");
                    _d = (_c = console).log;
                    return [4 /*yield*/, contract.storage()];
                case 4:
                    _d.apply(_c, [_e.sent()]);
                    console.log("Interacting with Smart Contract..");
                    console.log("First show the signature of the method");
                    console.log(contract.methodsObject.verifySig1().getSignature());
                    console.log("Now send a test transaction..");
                    contract.methodsObject.verifySig1({
                        message_packed: '6d6279746573',
                        pbk: 'edpkuYzXL37pTYVHu7rTodeyH9bQ2rfDKadWqqGCqL8m8G1W4UH55E',
                        provider_sig: 'edsigtffaz6wutLRzi7Ni15KPcoUZULJiyF3tHX78iBp17Fdt4jTTDmJjVe6QfK8ggimYGDcv7bLFziMPKSP2JxG5sb8NGKZcQG'
                    }).send().then(function (op) {
                        console.log("Awaiting for ".concat(op.hash, " to be confirmed..."));
                        return op.confirmation().then(function () { return op.hash; });
                    }).then(function (hash) { return console.log("Operation injected: https://hangzhou.tzstats.com/".concat(hash)); })["catch"](function (error) { return console.log("Error: ".concat(JSON.stringify(error, null, 2))); });
                    return [3 /*break*/, 6];
                case 5:
                    ex_1 = _e.sent();
                    console.log(ex_1);
                    return [3 /*break*/, 6];
                case 6: return [2 /*return*/];
            }
        });
    });
}
// tslint:disable-next-line: no-floating-promises
verify_sig();
