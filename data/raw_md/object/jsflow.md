---
description: 지도 내 바람 흐름을 표현하는 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSFlow

> Module.getFlow() API를 생성합니다.
>
> 입력 변수값은 [JSFlow.FlowDataOption](jsflow.md#jsflow.flowdataoption) 참조.

```javascript
let flow = Module.getFlow();
```

## Function

### ClearFlowData()

> 바람장 데이터 초기화

{% tabs %}
{% tab title="Information" %}

{% endtab %}

{% tab title="Template" %}

```javascript
let flow = Module.getFlow();
flow.ClearFlowData();
```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSFlow.FlowDataOption

> 바람 표현 입력 정보.

| Name   | Type                                                                             | Attributes | Default | Description       |
| ------ | -------------------------------------------------------------------------------- | ---------- | ------- | ----------------- |
| data   | [JSFlow.FlowDataOption.dataParam](jsflow.md#jsflow.flowdataoption.dataparam)     |            |         | 구성 데이터 필드. |
| option | [JSFlow.FlowDataOption.optionParam](jsflow.md#jsflow.flowdataoption.optionparam) | optional   |         | 초기 데이터 설정. |
| legend | [JSFlow.FlowDataOption.legendParam](jsflow.md#jsflow.flowdataoption.legendparam) | optional   |         | 범례 표현.        |

#### JSFlow.FlowDataOption.dataParam

> 구성 데이터 필드.

| Name | Type                                                                                 | Attributes | Default | Description                                                                   |
| ---- | ------------------------------------------------------------------------------------ | ---------- | ------- | ----------------------------------------------------------------------------- |
| url  | string                                                                               |            |         | 바람장 파일 url 경로.                                                         |
| dem  | [JSFlow.FlowDataOption.dataParam.dem](jsflow.md#jsflow.flowdataoption.dataparam.dem) | optional   |         | 바람장 분석시 저장파일 루트의 height.txt 파일을 파싱해서 미리 다운 받아 사용. |

#### JSFlow.FlowDataOption.dataParam.dem

> height.txt의 DEM 정보를 전환한 Float Array 데이터.

| Name     | Type   | Description                              |
| -------- | ------ | ---------------------------------------- |
| cols     | number | DEM 가로 셀수.                           |
| rows     | number | DEM 세로 셀수.                           |
| size     | number | DEM의 해상도 (단위 미터).                |
| llcorner | string | DEM의 좌하단 좌표 (GRS80 TM 중부, 60만). |
| data     | array  | DEM 데이터.                              |

#### JSFlow.FlowDataOption.dataParam.dem.llcorner

> DEM의 좌하단 좌표 (GRS80 TM 중부, 60만).

| Name     | Type   | Description                        |
| -------- | ------ | ---------------------------------- |
| left     | number | DEM 시작점의 x 좌표.               |
| lower    | number | DEM 시작점의 y 좌표.               |
| projCord | number | DEM 투영 데이터 크기(20으로 고정). |

#### JSFlow.FlowDataOption.optionParam

> 초기 데이터 설정.

| Name         | Type   | Description                                                          |
| ------------ | ------ | -------------------------------------------------------------------- |
| velocity     | number | 바람장 파티클 이동속도 스케일.                                       |
| offsetHeight | number | 바람장 파티클 높이 (DEM이 없으면 해발고도 기준, 있으면 지표면 기준). |
| maxParticle  | number | 화면에 최대 표출가능한 파티클 수 (5000 이하 권장).                   |
| minLifeTime  | number | 파티클 유지시간 최소 값.                                             |
| maxLifeTime  | number | 파티클 유지시간 최대 값 ( maxLifeTime > LifeTime > minLifeTime ).    |

#### JSFlow.FlowDataOption.legendParam

> 풍속별 범례를 적용하는 방법과 진행 궤적을 그라데이션으로 표현하는 방법이 있음.

-   풍속별 범례

| Name     | Type                                                                                               | Description                                 |
| -------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| maxIndex | number                                                                                             | 궤적 표현시 사용(풍속별 범례에선 255 고정). |
| fixValue | [JSFlow.FlowDataOption.legendParam.fixValue](jsflow.md#jsflow.flowdataoption.legendparam.fixvalue) | 풍속 기준 범례 사용 배열.                   |

-   진행 궤적 표현

| Name             | Type                                                                                       | Description                   |
| ---------------- | ------------------------------------------------------------------------------------------ | ----------------------------- |
| maxIndex         | number                                                                                     | 바람장 이동 속도.             |
| fixValue or band | [JSFlow.FlowDataOption.legendParam.band](jsflow.md#jsflow.flowdataoption.legendparam.band) | 풍속별 범례 또는 궤적 데이터. |

#### JSFlow.FlowDataOption.legendParam.fixValue

> 풍속 기준 범례 사용 배열.
>
> value와 color로 표현한 범례별 색상을 나열하여 배열에 저장(value 이하 풍속에서 color의 색상 적용).

| Name  | Type   | Description                                     |
| ----- | ------ | ----------------------------------------------- |
| value | number | 범례 풍속.                                      |
| color | array  | 해당 범례에 해당하는 색상 설정. r, g, b로 구성. |

#### JSFlow.FlowDataOption.legendParam.band

> 바람장 궤적 표현 배열.
>
> 전체 궤적을 maxIndex 구간으로 나누며, startIndex/endIndex을 통해 구간별로 색상을 지정.
>
> 배열에 나열된 start-end 색상 정보를 그라데이션 형태로 표현.
>
> ex) start: 빨강, end: 하양일 경우. 하양 ------------> 빨강

| Name       | Type   | Description                                |
| ---------- | ------ | ------------------------------------------ |
| startIndex | number | 구간을 반영할 시작부분 Table Index (꼬리). |
| startColor | array  | 꼬리에 해당하는 색상 설정. r, g, b로 구성. |
| endIndex   | number | 구간을 반영할 끝부분 Table Index (머리).   |
| endColor   | array  | 머리에 해당하는 색상 설정. r, g, b로 구성. |
