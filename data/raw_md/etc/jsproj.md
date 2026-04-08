---
description: 지도 내 좌표계 변환과 관련된 기능을 관리하기 위한 API 입니다.
---

# JSProj

> Module.JSProj() API를 생성합니다.
>
> 입력 값이 제공되지 않으면 기본값은 EPSG:4326입니다.
>
> [EPSG list](jsproj.md#epsg-coordinate-type-list) 이외도 PROJ4 코드 입력 시 전 세계 모든 좌표계를 사용할 수 있습니다. ([epsg.io 참조](https://epsg.io/)).

```javascript
let projection = new Module.JSProj(); // Defaults to epsg:4326
let projection = new Module.JSProj("EPSG code (epsg:4326)");
let projection = new Module.JSProj("PROJ4 code (+proj=longlat +datum=WGS84 +no_defs +type=crs)"); // PROJ4 code
```

## Function

### apply(code) → object

> PROJ4 코드를 통해 Projection을 재설정합니다.
>
> 이전 Projection을 초기화하고, 입력된 값으로 Projection을 생성합니다.

{% tabs %}
{% tab title="infomation" %}

| Name | Type   | Description       |
| ---- | ------ | ----------------- |
| code | string | EPSG, PROJ4 코드. |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 (문자열 : 실패 에러 코드).

{% endtab %}
{% tab title="Template" %}

```javascript
let projection = new Module.JSProj(); // Defaults to epsg:4326
let result = projection.apply("epsg:5186");
console.log(result); // Returns API result information
```

{% endtab %}
{% endtabs %}

### find(epsg) → object

> 엔진이 지원하는 투영 목록에 EPSG가 있는지 확인합니다.
>
> 입력된 EPSG 코드에 해당하는 PROJ4를 반환합니다.
>
> [EPSG list](jsproj.md#epsg-coordinate-type-list) 참조하세요.

{% tabs %}
{% tab title="infomation" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| epsg | string | EPSG 코드.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 (PROJ4 코드 : 정상적인 반환값, 문자열 : 실패 에러 코드).

{% endtab %}

{% tab title="Template" %}

```javascript
let projection = new Module.JSProj(); // Defaults to epsg:4326
let result = projection.find("epsg:5186");
console.log(result); // Returns API result information
```

{% endtab %}
{% endtabs %}

### getProjCode() → string

> JSProj 변수에 적용된 투영의 구성 요소인 proj4 코드를 반환합니다.

{% tabs %}
{% tab title="infomation" %}

-   Return
    -   API 결과 정보 반환(PROJ4 코드: 정상 반환 값, 공백: JSProj 초기화 상태).

{% endtab %}

{% tab title="Template" %}

```javascript
let projection = new Module.JSProj(); // Defaults to epsg:4326
let result = projection.getProjCode();
console.log(result); // Returns epsg:4326 proj4 code
// or
let projection = new Module.JSProj("epsg:5186"); // Defaults to epsg:4326
let result = projection.getProjCode();
console.log(result); // Returns epsg:5186 proj4 code
```

{% endtab %}
{% endtabs %}

### transform(option) → object

> 좌표 변환을 수행합니다.
>
> Projection을 기반으로 입력된 좌표를 변환합니다.

{% tabs %}
{% tab title="infomation" %}

| Name   | Type                                           | Description |
| ------ | ---------------------------------------------- | ----------- |
| option | [TransformOptions](jsproj.md#transformoptions) | 속성 정보.  |

-   Return

    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 (Array : 변환된 좌표 목록,, 문자열 : 실패 에러 코드).

-   Sample
    -   function transform 참조.
    -   [Sandbox_Coordinate Transformation](https://sandbox.egiscloud.com/code/main.do?id=others_coordinate_conversion)

{% endtab %}

{% tab title="Template" %}

```javascript
// Supports single transformation
let projection = new Module.JSProj(); // Defaults to epsg:4326
parameter = {
    source: "epsg:5186",
    coordinates: new Module.JSVector2D(200000.0, 378044.651253),
};
let result = projection.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
// or
let projection = new Module.JSProj(); // Defaults to epsg:4326
parameter = {
    source: "+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
    coordinates: new Module.JSVector3D(200000.0, 378044.651253, 10),
};
let result = projection.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
// or
// Supports Array type
let projection = new Module.JSProj(); // Defaults to epsg:4326
let coordinate = Array();
coordinate.push(new Module.JSVector3D(200000.0, 378044.651253, 10));
coordinate.push(new Module.JSVector3D(200000.0, 489012.95569100516, 10));
coordinate.push(new Module.JSVector3D(289012.929607278, 489480.463416938, 10));
parameter = {
    source: "epsg:5186",
    coordinates: coordinate,
};
let result = projection.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
```

{% endtab %}
{% endtabs %}

## Class Function

### list() → object

> 지도 내에서 등록된 Projection 목록을 사용자에게 제공합니다.
>
> 목록 정보는 EPSG 코드로 구성된 number Type 입니다.

{% tabs %}
{% tab title="infomation" %}

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 (Array : epsg 코드 목록 ).

{% endtab %}

{% tab title="Template" %}

```javascript
let list = Module.JSProj.list();
console.log(list); //epsg list
```

{% endtab %}
{% endtabs %}

### find(epsg) → object

> 지도 내에서 지원하는 Projection 목록 중 입력된 EPSG 코드 존재 유무를 확인합니다.
>
> 입력된 EPSG 코드를 통해 해당 PROJ4 코드를 반환합니다.
>
> [EPSG list](jsproj.md#epsg-coordinate-type-list) 참고.

{% tabs %}
{% tab title="infomation" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| epsg | string | EPSG 코드.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 (PROJ4 코드: 정상적인 반환값, 문자열 : 실패 에러 코드).

{% endtab %}
{% tab title="Template" %}

```javascript
let list = Module.JSProj.find("epsg:5186");
console.log(list); // Returns API result information
```

{% endtab %}
{% endtabs %}

### transform(option) → object

> 좌표 변환을 수행합니다.
>
> 입력 변수에 적용된 Projection으로 입력된 좌표를 변환합니다.

{% tabs %}
{% tab title="infomation" %}

| Name   | Type                                                     | Description |
| ------ | -------------------------------------------------------- | ----------- |
| option | [ClassTransformOptions](jsproj.md#classtransformoptions) | 속성 정보.  |

-   Return
    -   .result: API success status (1: Success, 0: Failure).
    -   .name: Operating API name.
    -   .return: API result information return (Array : 변환된 좌표 목록, 문자열 : 실패 에러 코드 ).

{% endtab %}

{% tab title="Template" %}

```javascript
// Supports single transformation
parameter = {
    target: "epsg:4326"
    source: "epsg:5186",
    coordinates: new Module.JSVector2D(200000.0, 378044.651253),
};
let result = Module.JSProj.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
// or
parameter = {
    target: "+proj=longlat +datum=WGS84 +no_defs",
    source: "+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
    coordinates: new Module.JSVector3D(200000.0, 378044.651253, 10),
};
let result = Module.JSProj.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
// or
// Supports Array type
let coordinate = Array();
coordinate.push(new Module.JSVector3D(200000.0, 378044.651253, 10));
coordinate.push(new Module.JSVector3D(200000.0, 489012.95569100516, 10));
coordinate.push(new Module.JSVector3D(289012.929607278, 489480.463416938, 10));
parameter = {
    target: "epsg:4326",
    source: "epsg:5186",
    coordinates: coordinate,
};
let result = Module.JSProj.transform(parameter); // Transforms coordinates from 5186 to 4326
console.log(result);
```

{% endtab %}
{% endtabs %}

## Type Definitions

#### TransformOptions

> 좌표 변환 옵션.

| Name        | Type                                                                                                                                                                                                                                    | Description             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| source      | string                                                                                                                                                                                                                                  | 원본 Projection 문자열. |
| coordinates | Array([JSVector2D](../core/jsvector2d.md), [JSVector3D](../core/jsvector3d.md)), [JSVector2D](../core/jsvector2d.md), [JSVector3D](../core/jsvector3d.md), [JSVec2Array](../core/jsvec2array.md), [JSVec3Array](../core/jsvec3array.md) | 변경 대상 위치 좌표     |

#### ClassTransformOptions

> 좌표 변환 옵션.

| Name        | Type                                                                                                                                                                                                                                    | Description             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| target      | string                                                                                                                                                                                                                                  | 변환 Projection 문자열. |
| source      | string                                                                                                                                                                                                                                  | 원본 Projection 문자열. |
| coordinates | Array([JSVector2D](../core/jsvector2d.md), [JSVector3D](../core/jsvector3d.md)), [JSVector2D](../core/jsvector2d.md), [JSVector3D](../core/jsvector3d.md), [JSVec2Array](../core/jsvec2array.md), [JSVec3Array](../core/jsvec3array.md) | 변경 대상 위치 좌표.    |

#### EPSG Coordinate Type List

> 국내에서 많이 사용하는 EPSG 목록입니다.
>
> 엔진 내부에서 EPSG:"번호"를 통해 EPSG에 goekdehlsms PROJ4 코드를 반환 가능합니다.
>
> 미지원 EPSG 코드인 경우 [epsg.io](https://epsg.io/)에서 제공되는 PROJ4 코드 입력시 사용 가능합니다.

| Index | Name       |
| ----- | ---------- |
| 2087  | epsg:2087  |
| 2096  | epsg:2096  |
| 2097  | epsg:2097  |
| 3857  | epsg:3857  |
| 4019  | epsg:4019  |
| 4044  | epsg:4044  |
| 4162  | epsg:4162  |
| 4166  | epsg:4166  |
| 4326  | epsg:4326  |
| 4737  | epsg:4737  |
| 5173  | epsg:5173  |
| 5174  | epsg:5174  |
| 5175  | epsg:5175  |
| 5176  | epsg:5176  |
| 5177  | epsg:5177  |
| 5178  | epsg:5178  |
| 5179  | epsg:5179  |
| 5180  | epsg:5180  |
| 5181  | epsg:5181  |
| 5182  | epsg:5182  |
| 5183  | epsg:5183  |
| 5184  | epsg:5184  |
| 5185  | epsg:5185  |
| 5186  | epsg:5186  |
| 5187  | epsg:5187  |
| 5188  | epsg:5188  |
| 32651 | epsg:32651 |
| 32652 | epsg:32652 |
