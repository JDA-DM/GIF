デジタル社会推進実践ガイドブック DS-439

> コアデータモデル解説書  
> 土地

2022年（令和4年）5月9日

デジタル庁

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>[キーワード]</p>
<p>土地、不動産、データモデル</p>
<p>[概要]</p>
<p>土地の情報をシステム実装する際に参照すべきデータモデルについて解説するガイドブックです。このガイドに従いデータ設計を行うことで、同じ設計規則に従うシステム間、分野間でのデータ連携を容易かつ正確に行えるようになります。また、データ設計を実施するコストも削減することができます。</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 土地のデータモデル

土地の情報を記述するためのデータモデルです。

必須項目以外は任意項目なので、用途に応じて項目を選択、あるいは独自項目を追加するなどのカスタマイズを行って利用してください。

### 土地データモデルの項目

土地データモデルの項目は表1の通りです。英語名や記入例などを含む詳細については、別添の「438_コアデータモデル_DMD.xlsx」を参照してください。

表1 土地データモデルの項目一覧

| 必須項目 | 項目名       | 説明                                                         |
|----------|--------------|--------------------------------------------------------------|
|          | ID           | 機械的に採番された土地を一意に識別するID。土地単位に付番する |
| 必       | 用途         | 土地の主要な用途                                             |
|          | 名称         | 土地の名称                                                   |
|          | 名称（カナ） | 土地のカナ表記                                               |
|          | 名称（英字） | 土地の英語名またはローマ字表記                               |
|          | 通称         | 土地に通称がある場合に記入                                   |
|          | 説明         | 土地情報として公開可能な詳細情報                             |
| 必       | 土地住所     | 住所情報（住所型）                                           |
|          | 敷地面積     | 土地の敷地面積(m2)                                           |
|          | ポリゴン     | 土地の形状を表す情報                                         |
|          | 備考         | 備考                                                         |
|          | 連絡先       | 連絡先の情報（連絡先型）                                     |

## 関連データ定義

### データモデルの関係性

土地は、IMIコア語彙や3D都市モデル標準性仕様書（CityGML）LandUseにも定義があります。その関係性を以下に示します。

表3 土地データモデルと関連モデルとの関係性

| GIFデータ項目 | 対応するIMI | 対応するCityGML |
|---------------|-------------|-----------------|
| ID            | ic:ID       |                 |
| 用途          | ic:主要用途 | luse:usage      |
| 名称          | ic:名称     | gml:name        |
| 名称（カナ）  | ic:名称     | gml:name        |
| 名称（英字）  | ic:名称     | gml:name        |
| 通称          | ic:通称     |                 |
| 説明          | ic:記述     | gml:description |
| 住所          | ic:住所     | bldg:address    |
| 面積          | ic:面積     | gml:MeasureType |
| ポリゴン      |             |                 |
| 備考          | ic:記述     |                 |
| 連絡先情報    | ic:連絡先   |                 |

### コントロールド・ボキャブラリ（統制語彙）

1.  ####### 用途

2.  ####### 土地の用途

> 都市計画基礎調査実施要領[^1]（平成 3 年 5 月国土交通省都市局）の土地コードの区分を使用する。

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>コード</p>
</blockquote></th>
<th><blockquote>
<p>説明</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td><blockquote>
<p>田（水田）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>畑（畑、樹園地、採草地、養鶏（牛・豚）場）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td><blockquote>
<p>山林（樹林地）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>204</p>
</blockquote></td>
<td><blockquote>
<p>水面（河川水面、湖沼、ため池、用水路、濠、運河水面）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td><blockquote>
<p>その他自然地（原野・牧野、荒れ地、低湿地、河川敷・河原、海浜、湖岸）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211</p>
</blockquote></td>
<td><blockquote>
<p>住宅用地（住宅、共同住宅、店舗等併用住宅、店舗等併用共同住宅、作業所併用住宅）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212</p>
</blockquote></td>
<td><blockquote>
<p>商業用地</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>213</p>
</blockquote></td>
<td><blockquote>
<p>工業用地</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>219</p>
</blockquote></td>
<td><blockquote>
<p>農林漁業施設用地</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>214</p>
</blockquote></td>
<td><blockquote>
<p>公益施設用地</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>215</p>
</blockquote></td>
<td><blockquote>
<p>道路用地（道路、駅前広場）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>216</p>
</blockquote></td>
<td><blockquote>
<p>交通施設用地</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>217</p>
</blockquote></td>
<td><blockquote>
<p>公共空地（公園・緑地、広場、運動場、墓園）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>218</p>
</blockquote></td>
<td><blockquote>
<p>その他公的施設用地（防衛施設用地）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>220</p>
</blockquote></td>
<td><blockquote>
<p>その他の空地①（ゴルフ場）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>221</p>
</blockquote></td>
<td><blockquote>
<p>その他空地②（太陽光発電のシステムを直接整備している土地）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>222</p>
</blockquote></td>
<td><blockquote>
<p>その他の空地③（平面駐車場）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>223</p>
</blockquote></td>
<td><blockquote>
<p>その他の空地④（その他の空地①～③以外の都市的土地利用：建物跡地、資材置場、改変工事中の土地、法面（道路、造成地等の主利用に含まれない法面））</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>231</p>
</blockquote></td>
<td><blockquote>
<p>不明</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>251</p>
</blockquote></td>
<td><blockquote>
<p>可住地</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>252</p>
</blockquote></td>
<td><blockquote>
<p>非可住地</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>260</p>
</blockquote></td>
<td><blockquote>
<p>農地（田、畑の区分がない）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>261</p>
</blockquote></td>
<td><blockquote>
<p>宅地（住宅用地、商業用地等の区分が無い）</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>262</p>
</blockquote></td>
<td><blockquote>
<p>道路・鉄軌道敷（道路と交通施設用地が混在）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>263</p>
</blockquote></td>
<td><blockquote>
<p>空地（その他の空地①～④の区分が無い）</p>
</blockquote></td>
</tr>
</tbody>
</table>

## 変更履歴

| 改定年月日   | 改定箇所 | 改定内容 |
|--------------|----------|----------|
| 2022年5月9日 | \-       | 初版決定 |

[^1]: https://www.mlit.go.jp/toshi/tosiko/kisotyousa001.html
