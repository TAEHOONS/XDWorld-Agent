---
description: 지도 내 레이어를 관리하기 위한 API 입니다.
---

# JSLayerList

> Module.JSLayerList() API를 생성합니다.

```javascript
let userlayer = new Module.JSLayerList(true); // Returns a user layer

let serverlayer = new Module.JSLayerList(false); // Returns a service layer
```

## Function

### count() → number

> 등록된 레이어 수를 반환합니다.
>
> 사용자 레이어, 서비스 레이어의 총 수 입니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 등록된 레이어의 총 수.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let count = layerList.count();
console.log(count);
```

{% endtab %}
{% endtabs %}

### createLayer(name, type) → [JSLayer](../layer/jslayer.md)

> 입력 변수값으로 레이어를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                                        |
| :--- | :----- | :------------------------------------------------- |
| name | string | 레이어 명칭.                                       |
| type | number | [Layer type.](../etc/type-list.md#layer-type-list) |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let layer = layerList.createLayer(“NewLayer”, Module.ELT_POLYHEDRON);
```

{% endtab %}
{% endtabs %}

### createObjectLayer(option) → [JSLayer](../layer/jslayer.md)

> 입력 변수값으로 사용자 레이어를 생성합니다.
>
> 사용자 레이어를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                                | Description |
| :----- | :------------------------------------------------------------------ | :---------- |
| option | [CreateObjectLayerOptions](jslayerlist.md#createobjectlayeroptions) | 속성 정보.  |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layer = Module.getObjectLayerList().createObjectLayer({
    name: "Layer Name",
    type: "Layer Type",
    visible: false,
    selectable: false,
    minDistance: 100.0,
    maxDistance: 1000.0,
});
```

{% endtab %}
{% endtabs %}

### createWFSLayer(name, type) → [JSLayer](../layer/jslayer.md)

> WFS 서비스 레이어를 생성합니다.
>
> Web Feature Server로 가시화 된 Tile 영역에 해당되는 오브젝트 요청.
>
> WFS 서비스 레이어로 new Module.JSLayerList( false ) 으로 생성합니다..

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                                          |
| :--- | :----- | ---------------------------------------------------- |
| Name | string | 레이어 명칭.                                         |
| type | number | [WFS layer type.](../etc/type-list.md#wfs-type-list) |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList( false );
let wfslayer = layerList.createWFSLayer( “WFS" , 0);
```

{% endtab %}
{% endtabs %}

### createWMSLayer( name ) → [JSLayer](../layer/jslayer.md)

> WMS 서비스 레이어를 생성합니다.
>
> Web Map Server로 가시화 된 Tile 영역에 해당되는 지형 영상 이미지 요청.
>
> WMS 서비스 레이어로 new Module.JSLayerList( false ) 으로 생성합니다..

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | ------------ |
| Name | string | 레이어 명칭. |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList( false );
let wmslayer = layerList.createWMSLayer( “WMS” );
```

{% endtab %}
{% endtabs %}

### createUserLayer(option) → [JSLayer](../layer/jslayer.md)

> 입력 변수값으로 사용자 타일 레이어를 생성합니다.
>
> 사용자 레이어를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                                | Description |
| :----- | :------------------------------------------------------------------ | :---------- |
| option | [CreateUserLayerOptions](jslayerlist.md#createuserlayeroptions)   | 속성 정보.  |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layer = Module.getTileLayerList().createUserLayer({
    name: "Layer Name",
    url: "Request Server Address",
    type: "Layer Type",
    visible: false,
    selectable: false,
    minLevel: 10,
    maxLevel: 14,
});
```

{% endtab %}
{% endtabs %}

### createXDServerLayer(option) → [JSLayer](../layer/jslayer.md)

> 입력 변수값으로 사용자/서비스 레이어를 생성합니다.
>
> 사용자/서비스 레이어를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                                    | Description |
| :----- | :---------------------------------------------------------------------- | :---------- |
| option | [CreateXDServerLayerOptions](jslayerlist.md#createxdserverlayeroptions) | 속성 정보.  |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 생성 성공.
    -   null : 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layer = Module.getTileLayerList().createXDServerLayer({
    name: "Layer Name",
    url: "Request Server Address",
    type: "Layer Type",
    visible: false,
    selectable: false,
    minLevel: 10,
    maxLevel: 14,
    ...
});
```

{% endtab %}
{% endtabs %}

### delLayerAtFirst() → boolean

> 등록된 레이어를 삭제합니다.
>
> JSLayerList에 포함된 레이어 목록 첫번째에 해당되는 레이어를 삭제합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 삭제 성공.
    -   false : 삭제 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let check = layerList.delLayerAtFirst();
console.log(check);
```

{% endtab %}
{% endtabs %}

### delLayerAtIndex(index) → boolean

> 등록된 레이어를 삭제합니다.
>
> JSLayerList에 포함된 레이어 목록에서 입력 변수값(index) 위치에 해당되는 레이어를 삭제합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| index | number | 인덱스 번호. |

-   Return
    -   true : 삭제 성공.
    -   false : 삭제 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);

let check = layerList.delLayerAtIndex(0);
check = layerList.delLayerAtName(0);
```

{% endtab %}
{% endtabs %}

### delLayerAtLast() → boolean

> 등록된 레이어를 삭제합니다.
>
> JSLayerList에 포함된 레이어 목록 마지막에 해당되는 레이어를 삭제합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 삭제 성공.
    -   false : 삭제 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let check = layerList.delLayerAtLast();
console.log(check);
```

{% endtab %}
{% endtabs %}

### delLayerAtName(name) → boolean

> 등록된 레이어를 삭제합니다.
>
> JSLayerList에 포함된 레이어 목록에서 입력 변수값(name)에 해당되는 레이어를 삭제합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | :----------- |
| name | string | 레이어 명칭. |

-   Return
    -   true : 삭제 성공.
    -   false : 삭제 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);

let check = layerList.delLayerAtName(“firstlayer”);
console.log(check);
check = layerList.delLayerAtName(“endlayer”);
console.log(check);
```

{% endtab %}
{% endtabs %}

### firstAtLayer() → [JSLayer](../layer/jslayer.md)

> 레이어를 반환합니다.
>
> JSLayerList에 포함된 레이어 목록 첫번째에 해당되는 레이어를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSLayer](../layer/jslayer.md) : 반환 성공.
    -   null : 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let result = layerList.firstAtLayer();
```

{% endtab %}
{% endtabs %}

### indexAtLayer(index) → [JSLayer](../layer/jslayer.md)

> 등록된 레이어를 반환합니다.
>
> JSLayerList에 포함된 레이어 목록에서 입력 변수값(index) 위치에 해당되는 레이어를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| index | number | 인덱스 번호. |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 반환 성공.
    -   null : 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let result = layerList.indexAtLayer(0);
result = layerList.indexAtLayer(1);
```

{% endtab %}
{% endtabs %}

### lastAtLayer() → [JSLayer](../layer/jslayer.md)

> 등록된 레이어를 반환합니다.
>
> JSLayerList에 포함된 레이어 목록 마지막에 해당되는 레이어를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSLayer](../layer/jslayer.md) : 반환 성공.
    -   null : 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let result = layerList.lastAtLayer();
```

{% endtab %}
{% endtabs %}

### layerAtIndex(layer) → number

> 입력 변수값(layer)의 인덱스 번호를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                           | Description |
| :---- | :----------------------------- | :---------- |
| layer | [JSLayer](../layer/jslayer.md) | 레이어.     |

-   Return
    -   result>0: 레이어 인덱스 번호.
    -   -1: JSLayerList에 포함된 레이어가 아닌 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let count = layerList.layerAtIndex(first);
console.log(count);
count = layerList.layerAtIndex(end);
console.log(count);
```

{% endtab %}
{% endtabs %}

### nameAtLayer(name) → [JSLayer](../layer/jslayer.md)

> 등록된 레이어를 반환합니다.
>
> JSLayerList에 포함된 레이어 목록에서 입력 변수값(name)과 명칭이 동일한 레이어를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | :----------- |
| name | string | 레이어 명칭. |

-   Return
    -   [JSLayer](../layer/jslayer.md) : 반환 성공.
    -   null : 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList( false );
let layer = layerList.nameAtLayer(“HybridLoad”);
```

{% endtab %}
{% endtabs %}

### setLayerMove(layer, type) → boolean

> 레이어 목록 순서를 변경합니다.
>
> 레이어 인덱스 순서를 move 조건으로 변경합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                           | Description                                               |
| :---- | :----------------------------- | :-------------------------------------------------------- |
| layer | [JSLayer](../layer/jslayer.md) | 레이어.                                                   |
| type  | boolean                        | <p>true: 인덱스 번호 증가.<br>false: 인덱스 번호 감소.<p> |

-   Return
    -   true : 변경 성공.
    -   false: 변경 실패.
    -   실패 조건
        -   등록된 레이어가 2개 미만인 경우.
        -   마지막 순서에 해당되는 레이어 순서를 뒤로 변경한 경우.
        -   첫 순서에 해당되는 레이어 순서를 앞으로 변경한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let check =  layerList.setLayerMove(end, true);
```

{% endtab %}
{% endtabs %}

### setLayerTopNBottom(layer, type) → boolean

> 레이어 목록 순서를 변경합니다.
>
> 레이어 인덱스 순서를 최상단, 최하단으로 변경합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                           | Description                                                                     |
| :---- | :----------------------------- | :------------------------------------------------------------------------------ |
| layer | [JSLayer](../layer/jslayer.md) | 레이어.                                                                         |
| type  | boolean                        | <p>true: 인덱스 번호 최상단으로 변경.<br>false: 인덱스 번호 최하단으로 변경.<p> |

-   Return
    -   true : 변경 성공.
    -   false: 변경 실패.
    -   실패 조건
        -   등록된 레이어가 2개 미만인 경우.
        -   마지막 순서에 해당되는 레이어 순서를 뒤로 변경한 경우.
        -   첫 순서에 해당되는 레이어 순서를 앞으로 변경한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(true);
let first = layerList.createLayer(“firstlayer”, Module.ELT_POLYHEDRON);
let second = layerList.createLayer(“secondlayer”, Module.ELT_POLYHEDRON);
let end = layerList.createLayer(“endlayer”, Module.ELT_POLYHEDRON);
let check =  layerList.setLayerMove(first, true);
```

{% endtab %}
{% endtabs %}

### getVisible(name) → number

> 레이어에 포함된 객체에 대한 가시화 유무를 반환합니다.
>
> 레이어가 투명/불투명 정보를 반환합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | :----------- |
| name | string | 레이어 명칭. |

-   Return
    -   1 : 레이어 포함 객체 가시화.
    -   0 : 레이어 포함 객체 비가시화.

{% endtab %}
{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(false);
let visible = layerList.getVisible(“HybridLoad”);
```

{% endtab %}
{% endtabs %}

### setVisible(name, type)

> 레이어에 포함된 객체에 대한 가시화 유무를 설정합니다.
>
> 레이어가 투명/불투명 정보를 설정합니다.
>
> 사용자 및 서비스 레이어 모두에서 사용할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                                |
| :--- | :------ | :------------------------------------------------------------------------- |
| name | string  | 레이어 명칭.                                                               |
| type | boolean | <p>true: 레이어 포함 객체 가시화.<br>false: 레이어 포함 객체 비가시화.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
let layerList = new Module.JSLayerList(false);
layerList.setVisible(“HybridLoad”, true);
layerList.setVisible(“HybridLoad”, false);
```

{% endtab %}
{% endtabs %}

## Type Definitions

#### CreateObjectLayerOptions

> 사용자 레이어 생성 옵션.

| Name        | Type                                                    | Attributes | Default | Description                            |
| ----------- | ------------------------------------------------------- | ---------- | ------- | -------------------------------------- |
| name        | String                                                  |            |         | 레이어 명칭.                           |
| type        | [Layer type List.](../etc/type-list.md#layer-type-list) |            |         | 레이어 타입.                           |
| visible     | boolean                                                 | optional   | true    | 레이어 가시화 옵션 설정.               |
| selectable  | boolean                                                 | optional   | true    | 레이어 포함된 오브젝트 선택 옵션 설정. |
| minDistance | number                                                  | optional   | 0.0     | 레이어 최소 가시 거리를 설정.          |
| maxDistance | number                                                  | optional   | 3000.0  | 레이어 최대 가시 거리를 설정.          |

#### CreateUserLayerOptions

> Options for creating a service layer.

| Name       | Type                                                    | Attributes | Default | Description                            |
| ---------- | ------------------------------------------------------- | ---------- | ------- | -------------------------------------- |
| name       | String                                                  |            |         | 레이어 명칭.                           |
| url        | String                                                  |            |         | 요청 서버 url.                         |
| type       | [Layer type List.](../etc/type-list.md#layer-type-list) |            |         | 레이어 타입.                           |
| visible    | boolean                                                 | optional   | true    | 레이어 가시화 옵션 설정.               |
| selectable | boolean                                                 | optional   | true    | 레이어 포함된 오브젝트 선택 옵션 설정. |
| minLevel   | number                                                  | optional   | 0       | 레이어 최소 가시 레벨를 설정.          |
| maxLevel   | number                                                  | optional   | 15      | 레이어 최대 가시 레벨를 설정.          |

#### CreateXDServerLayerOptions

> Options for creating a service layer.

| Name       | Type                                                    | Attributes | Default | Description                            |
| ---------- | ------------------------------------------------------- | ---------- | ------- | -------------------------------------- |
| name       | String                                                  |            |         | 레이어 명칭.                           |
| url        | String                                                  |            |         | 요청 서버 url.                         |
| type       | [Layer type List.](../etc/type-list.md#layer-type-list) |            |         | 레이어 타입.                           |
| visible    | boolean                                                 | optional   | true    | 레이어 가시화 옵션 설정.               |
| selectable | boolean                                                 | optional   | true    | 레이어 포함된 오브젝트 선택 옵션 설정. |
| minLevel   | number                                                  | optional   | 0       | 레이어 최소 가시 레벨를 설정.          |
| maxLevel   | number                                                  | optional   | 15      | 레이어 최대 가시 레벨를 설정.          |
| userLayer  | boolean                                                 | optional   | false   | 사용자 레이어 / 서비스 레이어.         |
| tileRatio  | number                                                  | optional   |         | LOD Ratio 값.                       |
| textureExt | String                                                  | optional   | "jpg"   | 텍스처 확장자(소문자).                |
| boundaryLimit | object                                               | optional   |         | Limit Boundary 설정.               |
| servername | String                                                  | optional   |         | 서버 이름 설정.                      |
| maxLevelOverlap | boolean                                            | optional   | false   | 하이브리드 레이어 최대레벨 초과 시 부모 참조 옵션 설정.|
| Authorization | boolean                                              | optional   | false   | 인증 토큰 fetch 방식 변경 플래그.      |