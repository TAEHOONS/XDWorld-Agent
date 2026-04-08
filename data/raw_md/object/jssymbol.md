---
description: 지도 내 jsicon 객체를 등록 및 관리하기 위한 API 입니다.
---

# JSSymbol

> Module.getSymbol() API를 생성합니다.

```javascript
var symbol = Module.getSymbol();
```

## Function

### getIcon(id) → [JSIcon](./jsicon.md)

> JSSymbol 등록된 [JSIcon](./jsicon.md) 객체를 반환합니다..

{% tabs %}
{% tab title="Name" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| id   | string | 고유 명칭.  |

-   Return
    -   [JSIcon](./jsicon.md): 반환 성공.
    -   null: 반환 실패.
    -   실패 조건
        -   입력 변수값(id)와 동일한 고유 명칭을 가진 [JSIcon](./jsicon.md) 객체가 없는 경우.
-   Sample
    -   the createPOI function 참조.
    -   [Sandbox_Height Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_altitude)

{% endtab %}
{% tab title="Template" %}

```javascript
var icon = Module.getSymbol.getIcon("Icon_name");
```

{% endtab %}
{% endtabs %}

### insertIcon(id, data, width, height) → boolean

> [JSIcon](./jsicon.md) 객체를 추가합니다.
>
> data 변수는 Uint8Array 기반의 바이너리 배열 데이터 입니다.
>
> 입력 변수값(width, height)은 이미지의 실제 크기 입니다.

{% tabs %}
{% tab title="Name" %}

| Name   | Type   | Description    |
| ------ | ------ | -------------- |
| id     | string | 고유 명칭.     |
| data   | object | 이미지 데이터. |
| width  | number | 이미지 너비.   |
| height | number | 이미지 높이.   |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
    -   실패 조건
        -   입력 변수값(id)와 동일한 고유 명칭을 가진 [JSIcon](./jsicon.md) 객체가 없는 경우.
        -   입력 변수값(data)이 null 인 경우.
        -   입력 변수값(width, height)이 0인 경우.
-   Sample
    -   the createPOI function 참조.
    -   [Sandbox_Height Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_altitude)

{% endtab %}
{% tab title="Template" %}

```javascript
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
//...render image on canvas...
var data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
Module.getSymbol.insertIcon("Icon_name", data, canvas.width, canvas.height);
```

{% endtab %}
{% endtabs %}

### deleteIcon(id) → boolean

> JSSymbol 등록된 [JSIcon](./jsicon.md) 객체를 삭제합니다.
>
> 입력 변수값(id)와 동일한 고유 명칭을 가진 [JSIcon](./jsicon.md) 객체를 삭제합니다.

{% tabs %}
{% tab title="Name" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| id   | string | 고유 명칭.  |

-   Return
    -   true: 삭제 성공.
    -   false: 삭제 실패.
    -   실패 조건
        -   입력 변수값(id)와 동일한 고유 명칭을 가진 [JSIcon](./jsicon.md) 객체가 없는 경우.
        -   해당 [JSIcon](./jsicon.md)를 참조 받는 객체가 하나 이상 존재하는 경우(참조 객체 삭제 후 재 동작).
-   Sample
    -   the clearAnalysis function 참조.
    -   [Sandbox_Height Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_altitude)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getSymbol.deleteIcon("Icon_name");
```

{% endtab %}
{% endtabs %}
